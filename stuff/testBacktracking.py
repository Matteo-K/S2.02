import time


def possible(grid, line, column):
    for id in range(line):
        if grid[id] == column:
            return False
        if grid[id] - id == column - line:
            return False
        if grid[id] + id == column + line:
            return False
    return True


def setQueen(grid, line, N):
    if line == N:
        return [grid[:]]
    solver = []
    for column in range(N):
        if possible(grid, line, column):
            grid[line] = column
            solver += setQueen(grid, line+1, N)
    return solver


def solverQueen(N):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    return setQueen(grid, 0, N)


comp = []
for n in [4, 8, 10, 12]:
    temps = 0
    for times in range(200):
        startTime = time.process_time()
        a = solverQueen(n)
        endTime = time.process_time()
        cpuTime = endTime - startTime
    comp += [n, cpuTime, len(a)]

print(comp)
