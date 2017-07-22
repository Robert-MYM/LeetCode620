class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #直接把上题算法改一改写成dfs,据说还有个什么跳舞链算法，暂不研究
        def valid(x, y):
            tmp = board[x][y]
            board[x][y] = 'D'
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
            board[x][y]=tmp
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j]=k
                            if valid(i,j) and dfs(board):
                                return True
                            board[i][j]='.'
                        return False
            return True
        dfs(board)