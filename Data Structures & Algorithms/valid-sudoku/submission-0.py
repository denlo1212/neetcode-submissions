class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for colum in range(9):
                boardNumber = board[row][colum]

                if boardNumber == ".":
                    continue

                if (boardNumber in rows[row] or
                    boardNumber in colums[colum] or
                    boardNumber in squares[row // 3, colum // 3]):
                    return False

                colums[colum].add(boardNumber)
                rows[row].add(boardNumber)
                squares[row // 3, colum // 3].add(boardNumber)
        return True
