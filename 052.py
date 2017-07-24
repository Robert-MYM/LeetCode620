class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        #参考csdn,写一个非递归回溯
        def check(m,n):
            for i in range(m):
                if board[i]==n or abs(m-i)==abs(board[i]-n):
                    return False
            return True
        board = [-1 for i in range(n)]
        col=0;row=0;sum=0
        while row<n:
            while col<n:
                if check(row,col):  #找row行的可以放的皇后
                    board[row]=col
                    col=0
                    break
                else:
                    col+=1
            if board[row] == -1:  # 没找到
                if row == 0:
                    break
                else:
                    row -= 1
                    col = board[row] + 1  # 线性回溯关键，让col从下一个col开始
                    board[row] = -1
                    continue
            if row == n - 1:  # 找到了一个
                sum += 1
                col = board[row] + 1  # 线性回溯关键，让col从下一个col开始
                board[row] = -1
                continue
            row+=1
        return sum