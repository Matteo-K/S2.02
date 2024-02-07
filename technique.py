import time
import random

def is_valid(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                return False
    return True

def solverRandom(size):
    progress = True
    while progress:
        values = list(range(size))
        res = []
        compteur = size-1
        while compteur > -1:
            id = random.randint(0,compteur)
            res.append(values.pop(id))
            compteur -= 1
        progress = False if is_valid(res) else True
    return res