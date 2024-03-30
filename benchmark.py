#!/bin/env -S python3 -O

"""
Program to benchmark N-Queen solver algorithms.
"""

from sys import stdout, stderr
from time import time
from typing import Iterable, Iterator, Collection
import json
import argparse as ap
import src.benchmarking as bch


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


if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(
        description='''
Benchmark N-Queen solver algorithms.

The resulting JSON is printed to standard output.''', epilog=bch.EPILOG,
        formatter_class=bch.RawTextArgumentDefaultsHelpFormatter)

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
    parser.add_argument('--indent', default=None,
                        type=bch.constrain(int, lambda n: n >= 0, 'indent must be non-negative'),
                        help='JSON indent')

    parser.add_argument('-c', '--count',
                        type=bch.constrain(int, lambda n: n > 0, 'count must be positive'),
                        help='benchmarking execution count')
    parser.add_argument('-d', '--duration',
                        type=bch.constrain(float, lambda t: t > 0, 'duration must be positive'),
                        help='benchmarking duration (seconds)')

    args = parser.parse_args()

    # Extract chosen algorithms
    chosen_algorithms: set[str] = set()
    for regex in args.algorithms:
        matched_algorithms = tuple(bch.match_algorithms(regex))
        if len(matched_algorithms) == 0:
            parser.error(f'no algorithm matching "{regex}".')
        chosen_algorithms.update(matched_algorithms)

    if args.n_interval[1] is None:  # If N is unbounded
        if args.count is None or args.duration is None:
            parser.error("the maximum value of N isn't specified; benchmarking count and duration must be specified")

        results = list(benchmark_unbounded_n(chosen_algorithms, args.n_interval[0],
                                             bch.CountBenchmarkingStrategy(args.count),
                                             args.duration))
    else:
        if (args.count is None) == (args.duration is None):
            parser.error("the maximum value of N is specified; benchmarking count or duration (only one of the two) must be specified")

        n_range = range(args.n_interval[0], args.n_interval[1] + 1)
        results = benchmark_bounded_n(chosen_algorithms, n_range,
                                      bch.CountBenchmarkingStrategy(args.count)
                                      if args.duration is None else
                                      bch.DurationBenchmarkingStrategy(
                                          args.duration / len(chosen_algorithms) / len(n_range)))

    benchmark = bch.Benchmark(args.n_interval[0],
                                 {algorithm: result
                                  for algorithm, result in zip(chosen_algorithms, results, strict=True)})
    if args.verbose:
        print('Benchmark completed. Dumping JSON...', file=stderr)

    json.dump(benchmark, stdout, default=vars, indent=args.indent)
