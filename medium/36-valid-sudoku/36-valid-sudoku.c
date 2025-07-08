                    return False
                if val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]:
                    continue
                if val == ".":
                val = board[r][c]
            for c in range(9):
        for r in range(9):
        boxes = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set)
    def isValidSudoku(self, board):
class Solution(object):