class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        matrix=[[-1 for row in range(n)] for col in range(n)]
        k=(n+1)/2
        count=1
        for i in range(k):
            row = i
            col = i
            if (n - 2 * i) == 1:
                while row < n - i:
                    matrix[row][col]=count
                    count+=1
                    row += 1
                return matrix
            if (n - 2 * i) == 1:
                while col < n - i:
                    matrix[row][col]=count
                    count+=1
                    col += 1
                return matrix
            while col < n - i - 1:
                matrix[row][col]=count
                count+=1
                col += 1
            while row < n - i - 1:
                matrix[row][col]=count
                count+=1
                row += 1
            while col > i and col < n:
                matrix[row][col]=count
                count+=1
                col -= 1
            while row > i and row < n:
                matrix[row][col]=count
                count+=1
                row -= 1
        return matrix

