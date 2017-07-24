class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #[1,2,3],[4,5,6],[7,8,9]
        #转置 [1,4,7],[2,5,8],[3,6,9]
        #翻转[7,4,1][8,5,2][9,6,3]
        #矩阵旋转90度等价于转置后按行翻转
        ls=len(matrix)
        for i in range(ls):
            for j in range(i+1,ls):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(ls):
            matrix[i].reverse()



