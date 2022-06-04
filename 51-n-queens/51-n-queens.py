class Solution:
    def availableSquares(self, board: List[int], row: int):
        n = len(board)
        columns, downDiagonals, upDiagonals = 0, 0, 0
        
        for i, j in enumerate(board):
			# there is a queen at j in row i
            if j != 0:
                columns |= 1 << j - 1
                downDiagonals |= 1 << i - j + n
                upDiagonals |= 1 << i + j - 1
        
        for j in range(n):
			# if square j in row is not blocked
            if columns & 1 << j == 0 and downDiagonals & 1 << (row - j + n - 1) == 0 and upDiagonals & 1 << (row + j) == 0:
                yield j + 1
    
    def backtrack(self, board: List[int], k: int = 0,):
        n = len(board)
        if k == n:
			# we've successfully placed n queens on the board, append board to solutions
            self.solutions.append(["".join("Q" if i == rowQ else "." for i in range(1, n + 1)) for rowQ in board])
        else:
			# for each available square in row k
            for j in self.availableSquares(board, k):
                board[k] = j                  # add queen at position j in row k
                self.backtrack(board, k + 1)  # move on to the next row
                board[k] = 0                  # remove queen from row k
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.backtrack([0 for _ in range(n)])
        return self.solutions