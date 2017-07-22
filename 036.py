class Solution(object):
    #这是O(n^2)的算法 其实还有O（n）的运用字典的算法，字典的算法使用的空间复杂度较大，想想都差不多，就取了这个

    def valid(self, x, y, tmp, board):
        for i in range(9):
            if board[i][y] == tmp:
                return False
        for j in range(9):
            if board[x][j] == tmp:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x / 3) * 3 + i][(y / 3) * 3 + j] == tmp:
                    return False
        return True

    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                tmp = board[i][j]
                board[i][j] = 'D'
                if self.valid(i, j, tmp, board) == False:
                    return False
                else:
                    board[i][j] = tmp
        return True