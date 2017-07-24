class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #经典回溯法,递归
        def check(m,n):
            for i in range():
                if board[i]==n or abs(m-i)==abs(board[i]-n):
                    return False
            return True
        def dfs(depth,valuelist):
            if depth==n:
                res.append(valuelist)
                return
            for j in range(n):
                if check(depth,j):
                    board[depth]=j
                    s='.'*n
                    dfs(depth+1,valuelist+[s[:j]+'Q'+s[j+1:]])
        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res