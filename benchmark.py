#!/bin/env -S python3 -O

from sys import stderr
import tracemalloc
import time
import argparse
from statistics import mean, median
from importlib import import_module
from solver import Solver
from src.board import Board
import matplotlib.pyplot as plt