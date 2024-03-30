#!/bin/env bash

set -euo pipefail

readonly count=100
readonly duration=120

for algorithm in backtracking_graphe backtracking brute_force swap mask min_conflicts pingpong random symetrie; do
    file_json="benchmarks/json/$algorithm.json"
    file_md="doc/$algorithm.md"
    #./benchmark.py - $algorithm -v -c $count -d $duration > $file_json
    #echo -e '\n## Benchmark\n' >> $file_md
    #./graph.py mermaid time --markdown -t "Temps CPU - $algorithm ($count essais)" < $file_json >> $file_md
    echo >> $file_md
    ./graph.py mermaid mem --markdown -t "Mémoire - $algorithm ($count essais)" < $file_json >> $file_md
done