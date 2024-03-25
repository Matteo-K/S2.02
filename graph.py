#!/bin/env -S python3 -O

"""
Program to create MPL benchmarking charts of N-Queen solver algorithms.
"""

from dataclasses import dataclass
from sys import stderr
from typing import Any, Sequence, Callable
import argparse as ap
import matplotlib.pyplot as plt
import src.benchmarking as bench


def transform_char(string: str, index: int, transform: Callable[[str], str]) -> str:
    return string[:index] + transform(string[index]) + string[index + 1:]


class FieldsArgumentParser:
    def __init__(self, fields: Sequence[str]):
        # Find the field letter index
        for i in range(min(map(len, fields))):
            if len({field[i] for field in fields}) == len(fields) and all(field[i].isalpha() for field in fields):
                self.__i = i
                break
        else:
            raise ValueError("Couldn't find an index for distinct field letters")
        self.__fields = {field[self.__i].casefold(): field for field in fields}

    def unparse(self, show_fields: dict[str, bool]) -> str:
        if list(show_fields.keys()) != list(self.__fields.values()):
            raise ValueError('The fields in show_fields are different from the ones this object was initialized with')

        return ''.join(field[self.__i].upper() if show else field[self.__i].lower() for field, show in show_fields.items())

    def parse(self, field_arg: str) -> dict[str, bool]:
        if len(field_arg) != len(self.__fields):
            raise ValueError('field_arg is not of the correct length')
        if not field_arg.isalpha():
            raise ValueError('field_arg is not alphabetic')

        return {self.__fields[l.casefold()]: l.isupper() for l in field_arg}

    def add_argument(self, parser: ap.ArgumentParser, short_name: str, long_name: str, defaults: dict[str, bool]) -> str:
        helpstring = 'show (uppercase), or hide (lowercase) fields:\n' + ''.join(
            f'  {letter} as in {transform_char(name, self.__i, lambda l: l.upper())}\n'
            for letter, name in self.__fields.items())
        parser.add_argument(short_name, long_name, default=fields_parser.unparse(defaults),
                            help=helpstring)


if __name__ == '__main__':
    criteria = {
        # Keys are BenchmarkResult attribute suffixes
        'mem': ('Memory', 'bytes'),
        'time': ('CPU time', 'ms'),
    }

    fields = {
        # Keys are BenchmarkResult attribute prefixes
        'average': 'avg',
        'median': 'med',
        'min': 'min',
        'max': 'max',
    }

    DEFAULT_SHOWN_FIELDS = {
        'average': True,
        'median': False,
        'min': False,
        'max': False,
    }

    fields_parser = FieldsArgumentParser(fields.keys())

    @dataclass(frozen=True)
    class ResultAttribute:
        criterion: str
        field: str

        @property
        def class_attribute(self):
            return f'{fields[self.field]}_{self.criterion}'

        def humanize(self, algorithm: str) -> str:
            return f'{algorithm} {self.field}'
    # Parse arguments
    parser = ap.ArgumentParser(
        description='Create MPL graphs of N-Queens problem solver algorithms benchmarks.', epilog='S2.02', formatter_class=bench.RawTextArgumentDefaultsHelpFormatter)

    parser.add_argument('criterion', choices=criteria.keys(),
                        help='performance criterion')
    parser.add_argument('nmin', type=int,
                        help='minimal value of N. 4 is the minimum value for which a solution exists, excluding 0 and 1')
    parser.add_argument('nmax', type=int,
                        help='maximal value of N')
    parser.add_argument('algorithms', nargs='+', metavar='ALGORITHM',
                        help='algorithms to benchmark (each one will have its own colored curve). Supports regular expressions.\nAvailable algorithms:\n' + '\n'.join(f'  {algorithm}' for algorithm in bench.ALGORITHMS))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')

    # Graph options
    parser.add_argument('-t', '--title',
                        help='generated graph title. A title will be generated if this option not specified')
    parser.add_argument('-s', '--scale', choices={'linear', 'log', 'symlog', 'logit'}, default='linear',
                        help='the MPL scale to use on the Y axis')
    fields_parser.add_argument(parser, '-f', '--fields', DEFAULT_SHOWN_FIELDS)

    # Benchmarking options
    benchmarking_group = parser.add_mutually_exclusive_group()

    benchmarking_group.add_argument('-b', '--times', default=200, type=int,
                                          help='benchmark execution count')
    benchmarking_group.add_argument('-d', '--duration', type=float,
                                          help='benchmark duration (seconds)')

    args = parser.parse_args()

    if args.nmin < 4:
        bench.args_error(f'NMIN ({args.nmin}) must be at least 4')
    if args.nmin > args.nmax:
        bench.args_error(f'NMIN ({args.nmin}) is greater than NMAX ({args.nmax})')

    show_field = fields_parser.parse(args.fields)

    n_values = range(args.nmin, args.nmax + 1)

    chosen_algorithms = set()
    for regex in args.algorithms:
        matched_algorithms = tuple(bench.match_algorithms(regex))
        if len(matched_algorithms) == 0:
            bench.args_error(f'no algorithm matching "{regex}".')
        chosen_algorithms.update(matched_algorithms)

    benchmarking_strategy = bench.DurationBenchmarkingStrategy(
        args.duration / len(chosen_algorithms) / len(n_values)) if args.duration else bench.NumberOfTimesBenchmarkingStrategy(args.times)

    relevant_result_attributes = {ResultAttribute(args.criterion, field) for field in fields if show_field[field]}

    # Run benchmarks
    results = {}
    for algorithm in chosen_algorithms:
        solver = bench.get_solver(algorithm)
        benchmark_results = []
        for n in n_values:
            if args.verbose:
                print(f'{algorithm} n={n}...', file=stderr)
            benchmark_results.append(bench.benchmark(n, solver, args.verbose, benchmarking_strategy))
        for rra in relevant_result_attributes:
            results[rra.humanize(algorithm)] = [getattr(result, rra.class_attribute) for result in benchmark_results]

    # Configure graph
    plt.title(args.title or f'{criteria[args.criterion][0]} benchmarking of {", ".join(chosen_algorithms)}')
    plt.ylabel(f'{criteria[args.criterion][0]} ({criteria[args.criterion][1]})')
    plt.xlabel('N')
    plt.yscale(args.scale)
    for label, row in results.items():
        plt.plot(n_values, row, label=label)
    plt.legend()
    plt.show()
