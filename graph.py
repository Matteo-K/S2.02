#!/bin/env -S python3 -O

"""
Program to create MPL benchmarking charts of N-Queen solver algorithms.
"""

from dataclasses import dataclass
from sys import stderr
from time import time
from typing import Iterable, Iterator, Collection
import argparse as ap
import src.benchmarking as bch


@dataclass(frozen=True)
class ResultAttribute:
    criterion: str
    field: str

    @property
    def class_attribute(self):
        return f'{FIELDS[self.field]}_{self.criterion}'


def benchmark_unbounded_n(algorithms: Collection[str], min_n: int, benchmarking_strategy: bch.BenchmarkingStrategy, total_duration: float) -> Iterator[list[bch.BenchmarkResult]]:
    duration_per_algorithm = total_duration / len(algorithms)
    for algorithm in algorithms:
        solver = bch.get_solver(algorithm)
        n = min_n
        benchmark_results = []
        start_instant = time()
        while time() - start_instant < duration_per_algorithm:
            if args.verbose:
                print(f'{algorithm} n={n}...', file=stderr)
            benchmark_results.append(bch.benchmark(n, solver, args.verbose, benchmarking_strategy))
            n += 1
        yield benchmark_results


def benchmark_bounded_n(algorithms: Iterable[str],
                        n_range: range, benchmarking_strategy: bch.BenchmarkingStrategy) -> Iterator[list[bch.BenchmarkResult]]:
    for algorithm in algorithms:
        solver = bch.get_solver(algorithm)
        benchmark_results = []
        for n in n_range:
            if args.verbose:
                print(f'{algorithm} n={n}...', file=stderr)
            benchmark_results.append(bch.benchmark(n, solver, args.verbose, benchmarking_strategy))
        yield benchmark_results


CRITERIA = {
    # Keys are BenchmarkResult attribute suffixes
    'mem': ('Memory', 'bytes'),
    'time': ('CPU time', 'ms'),
}

FIELDS = {
    # Values are BenchmarkResult attribute prefixes
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

if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(
        description='Create MPL graphs of N-Queens problem solver algorithms benchmarks.', epilog='S2.02',
        formatter_class=bch.RawTextArgumentDefaultsHelpFormatter)


# [N]- : start at N (default 4), requires duration and count
# [N]-M : from n (default 4) to m, requires duration or count

# graph.py {mem, time} {duration, count, n-values}
# graph.py time --duration 60 --count 200 # get to maximum n with these parameters
# graph.py time 4-10 --count 60 --n-values
#

    parser.add_argument('criterion', choices=CRITERIA.keys(),
                        help='performance criterion\n\n')
    parser.add_argument('n_interval', type=bch.interval_arg_type(4, '-'), metavar='N-INTERVAL',
                        help='''N value interval.
With maximum specified (count xor duration have to be specified):
  -M       from 4 to M
  N-M      from N to M

With maximum unspecified (count and duration have to be specified):
  N        start at N
  N-       start at N

N must be at least 4 (the minimum value for which a solution exists, excluding 0 and 1).

''')
    parser.add_argument('algorithms', nargs='+', metavar='ALGORITHM', type=bch.constrain(
        str, bch.re_is_valid, 'algorithm must be a valid Python regular expression'),
        help='algorithms to benchmark (each one will have its own colored curve). Supports regular expressions.\nAvailable algorithms:'
        + ''.join(f'\n  {algorithm}' for algorithm in bch.ALGORITHMS))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')

    # Graph options
    options_graph = parser.add_argument_group('Graph options')
    options_graph.add_argument('-t', '--title',
                               help='generated graph title. A title will be generated if this option not specified')
    options_graph.add_argument('-s', '--scale', choices={'linear', 'log', 'symlog', 'logit'}, default='linear',
                               help='the MPL scale to use on the Y axis')
    options_graph.add_argument('-f', '--fields', action=bch.fields_arg(FIELDS.keys()), default=DEFAULT_SHOWN_FIELDS)

    # Benchmarking options
    options_benchmarking = parser.add_argument_group('Benchmarking options')
    options_benchmarking.add_argument('-c', '--count',
                                      type=bch.constrain(int, lambda n: n > 0, 'execution count must be greater than zero'),
                                      help='benchmarking execution count')
    options_benchmarking.add_argument('-d', '--duration',
                                      type=bch.constrain(float, lambda t: t > 0, 'duration must be greater than zero'),
                                      help='benchmarking duration (seconds)')

    args = parser.parse_args()

    # Extract chosen algorithms
    chosen_algorithms = set()
    for regex in args.algorithms:
        matched_algorithms = tuple(bch.match_algorithms(regex))
        if len(matched_algorithms) == 0:
            parser.error(f'no algorithm matching "{regex}".')
        chosen_algorithms.update(matched_algorithms)

    # Extract relevant result attributes
    relevant_result_attributes = {ResultAttribute(args.criterion, field) for field in FIELDS if args.fields[field]}

    if args.n_interval[1] is None:  # If N is unbounded
        if args.count is None or args.duration is None:
            parser.error("the maximum value of N isn't specified; benchmarking count and duration must be specified")

        results = list(benchmark_unbounded_n(chosen_algorithms, args.n_interval[0],
                                        bch.CountBenchmarkingStrategy(args.count),
                                        args.duration))
        n_range = range(args.n_interval[0], len(results[0]) + args.n_interval[0])
    else:
        if (args.count is None) == (args.duration is None):
            parser.error("the maximum value of N is specified; benchmarking count or duration (only one of the two) must be specified")

        n_range = range(args.n_interval[0], args.n_interval[1] + 1)
        results = benchmark_bounded_n(chosen_algorithms, n_range,
                                      bch.CountBenchmarkingStrategy(args.count)
                                      if args.duration is None else
                                      bch.DurationBenchmarkingStrategy(
                                          args.duration / len(chosen_algorithms) / len(n_range)))

    result_data = {f'{rra.field} {algorithm}': tuple(getattr(result, rra.class_attribute)
                                                     for result in benchmark_results)
                   for algorithm, benchmark_results in zip(chosen_algorithms, results, strict=True)
                   for rra in relevant_result_attributes}

    if args.verbose:
        print('Benchmark completed, creating plot...', file=stderr)

    # MPL takes time to load, so only import it when needed
    import matplotlib.pyplot as plt

    # Configure graph
    plt.title(args.title or f'{CRITERIA[args.criterion][0]} benchmarking of {", ".join(chosen_algorithms)}')
    plt.ylabel(f'{CRITERIA[args.criterion][0]} ({CRITERIA[args.criterion][1]})')
    plt.xlabel('N')
    plt.yscale(args.scale)
    for label, row in result_data.items():
        plt.plot(n_range, row, label=label)
    plt.legend()
    plt.show()
