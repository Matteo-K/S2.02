class Board:
    def __init__(self, n: int):
        self._n = n
        self._board = [[True for _ in range(n)] for _ in range(n)]

    @property
    def n(self) -> int:
        return self._n

    def __getitem__(self, index: tuple[int, int]) -> bool:
        return self._board[index[0]][index[1]]

    def __setitem__(self, index: tuple[int, int], value: bool):
        self._board[index[0]][index[1]] = value

    def __str__(self):
        return '\n'.join(''.join('.' if cell else 'O' for cell in row) for row in self._board)
