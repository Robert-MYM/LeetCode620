class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0: return res
        n = len(matrix[0])
        if n == 0: return res
        k = min((m + 1) / 2, (n + 1) / 2)
        for i in range(k):
            row = i;
            col = i
            if (n - 2 * i) == 1:
                while row < m - i:
                    res.append(matrix[row][col])
                    row += 1
                return res
            if (m - 2 * i) == 1:
                while col < n - i:
                    res.append(matrix[row][col])
                    col += 1
                return res
            while col < n - i - 1:
                res.append(matrix[row][col])
                col += 1
            while row < m - i - 1:
                res.append(matrix[row][col])
                row += 1
            while col > i and col < n:
                res.append(matrix[row][col])
                col -= 1
            while row > i and row < m:
                res.append(matrix[row][col])
                row -= 1
        return res
