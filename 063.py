class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            else:
                return 0
        else:
            if obstacleGrid[0][0] == 1:
                obstacleGrid[0][0] = 0
            else:
                obstacleGrid[0][0] = 1
            for i in range(1, m):
                if obstacleGrid[i][0] == 1:
                    obstacleGrid[i][0] = 0
                else:
                    obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            for j in range(1, n):
                if obstacleGrid[0][j] == 1:
                    obstacleGrid[0][j] = 0
                else:
                    obstacleGrid[0][j] = obstacleGrid[0][j - 1]
            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]