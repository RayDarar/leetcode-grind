class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def valid_row(i: int) -> bool:
            table: set[str] = set()
            for n in board[i]:
                if n == ".":
                    continue
                if n in table:
                    return False
                table.add(n)
            return True

        def valid_col(j: int) -> bool:
            table: set[str] = set()
            for i in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                if n in table:
                    return False
                table.add(n)
            return True

        def valid_block(i_start: int, j_start: int) -> bool:
            table: set[str] = set()
            for i in range(i_start, i_start + 3):
                for j in range(j_start, j_start + 3):
                    n = board[i][j]
                    if n == ".":
                        continue
                    if n in table:
                        return False
                    table.add(n)
            return True

        for i in range(9):
            if not valid_row(i):
                return False
            if not valid_col(i):
                return False

        for i, j in [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]:
            if not valid_block(i, j):
                return False

        return True


Solution().isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
