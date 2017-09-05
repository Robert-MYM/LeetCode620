class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #DP
        if n==0:return 0
        if n==1:return 1
        if n==2:return 2
        if n==3:return 3
        res=self.climbStairs(n-2)*2+self.climbStairs(n-3)
        return res