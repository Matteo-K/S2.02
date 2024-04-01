#!/bin/env -S python3 -O

"""
Program to create MPL or Mermaid representations of benchmarks.
"""

from html import escape
from sys import stdin, stdout
from warnings import warn
import argparse as ap
import json
import src.benchmarking as bch

CRITERIA = {
    # Keys are BenchmarkResult attribute suffixes
    'mem': ('Mémoire', 'octets'),
    'time': ('Temps CPU', 'ms'),
}

FIELD_NAMES = {
    # Values are BenchmarkResult attribute prefixes
    'avg': 'moyenne',
    'med': 'médiane',
    'min': 'min.',
    'max': 'max.',
}


def generate_mpl(benchmark: bch.Benchmark, fields: dict[str, bool], criterion: str,
                 *, title: str, xlabel: str, ylabel: str, scale: str):
    # MPL takes time to load, so only import it when needed
    import matplotlib.pyplot as plt

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale(scale)
    for algorithm, results in benchmark.result.items():
        for field in (field for field, show in fields.items() if show):
            plt.plot(range(benchmark.min_n, benchmark.min_n + len(results)),
                     [result[f"{field}_{criterion}"] for result in results],
                     label=f'{algorithm} {FIELD_NAMES[field]}')
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    plt.savefig(stdout.buffer, bbox_inches='tight')


def generate_mermaid(benchmark: bch.Benchmark, fields: dict[str, bool], criterion: str,
                     *, title: str, xlabel: str, ylabel: str, scale: str,
                     markdown_friendly: bool = False):
    if scale != 'linear':
        raise ValueError(f'Mermaid XY charts currently only support the linear scale, but the "{scale}" scale was specified.')
    line_count = len(benchmark.result) * sum(fields.values())
    if line_count > 1:
        warn(
            f'Warning: Mermaid XY charts currently offer no support for line labels. The graph will contain {line_count} lines only distinguished by color.')

    if markdown_friendly:
        print('```mermaid')
    print('xychart-beta')
    print(f'title "{escape(title)}"')
    print(f'x-axis "{escape(xlabel)}" {benchmark.min_n} --> {benchmark.min_n + max(map(len, benchmark.result.values()))}')
    print(f'y-axis "{escape(ylabel)}"')
    for algorithm, results in benchmark.result.items():
        for field in (field for field, show in fields.items() if show):
            print(
                f'line "{escape(algorithm)} {escape(FIELD_NAMES[field])}" [{", ".join(str(result[f"{field}_{criterion}"]) for result in results)}]')
    if markdown_friendly:
        print('```')


DEFAULT_SHOWN_FIELDS = {
    'avg': True,
    'med': False,
    'min': False,
    'max': False,
}

if __name__ == '__main__':
    prog_description = '''Create MPL or Mermaid representations of benchmarks.

The benchmark JSON is read from standard input.
The result is printed to standard output.'''
    parent = ap.ArgumentParser(add_help=False)
    parent.add_argument('criterion', choices=CRITERIA.keys(),
                        help='performance criterion\n\n')

    parent.add_argument('-t', '--title',
                        help='generated graph title. A title will be generated if this option not specified')
    parent.add_argument('-s', '--scale', choices={'linear', 'log', 'symlog', 'logit'}, default='linear',
                        help='the MPL scale to use on the Y axis')
    parent.add_argument('-f', '--fields', action=bch.fields_arg(FIELD_NAMES.keys()), default=DEFAULT_SHOWN_FIELDS)

    parser = ap.ArgumentParser()
    subparsers = parser.add_subparsers(title='Representations', dest='representation', required=True)

    parser_mpl = subparsers.add_parser('mpl', parents=[parent], description=prog_description,
                                       help='MatplotLib plot PNG', epilog=bch.EPILOG)

    parser_mermaid = subparsers.add_parser('mermaid', parents=[parent], description=prog_description,
                                           help='Mermaid XY chart', epilog=bch.EPILOG)
    parser_mermaid.add_argument('-m', '--markdown', action='store_true',
                                help='Markdown-friendly output: enclose Mermaid in code block')

    args = parser.parse_args()

    benchmark = bch.Benchmark(*json.load(stdin).values())

    common_args = {
        'benchmark': benchmark,
        'fields': args.fields,
        'criterion': args.criterion,
        'title':  args.title or f'{CRITERIA[args.criterion][0]} - {", ".join(benchmark.result.keys())}',
        'xlabel': 'N',
        'ylabel': f'{CRITERIA[args.criterion][0]} ({CRITERIA[args.criterion][1]})',
        'scale': args.scale,
    }

    match args.representation:
        case 'mpl':
            generate_mpl(**common_args)
        case 'mermaid':
            generate_mermaid(**common_args, markdown_friendly=args.markdown)
        case other:
            assert False, f'{other} is not a known representation'
