class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.dp(m,n)

    def dp(self,m,n):  #直接暴力动规TLE了 需要用数组优化
        if m==0:return 0
        if n==0:return 0
        if m==1:return 1
        if n==1:return 1
        return self.dp(m-1,n)+self.dp(m.n-1)