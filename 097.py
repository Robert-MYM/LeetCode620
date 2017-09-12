class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #直接试了试暴力的算法，99/101passed，后面2个TLE了，之后改用DP
        """
        if len(s1) + len(s2) != len(s3): return False
        if len(s3) == 0: return True
        if len(s1) == 0:
            if s2 == s3:
                return True
            else:
                return False
        if len(s2) == 0:
            if s1 == s3:
                return True
            else:
                return False
        if s1[0] == s3[0] and s2[0] != s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s1[0] != s3[0] and s2[0] == s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        elif s1[0] == s3[0] and s2[0] == s3[0]:
            return (self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]))
        else:
            return False
        """
        if len(s1) + len(s2) != len(s3): return False
        a=len(s1);b=len(s2)
        dp=[[False for i in range(b+1)] for j in range(a+1)]
        dp[0][0]=True
        for i in range(1,a+1):dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,b+1):dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,a+1):
            for j in range(1,b+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[a][b]