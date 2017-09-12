class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #DFS版本，答案正确但是TLE
        self.res=0
        return self.res
    def dfs(self,s,t):
        if len(t)==0 or len(s)==0:return
        if len(t)==1 and s[0]==t[0]:
            self.res+=1
            return
        if s[0]==t[0]:
            self.dfs(s[1:],t[1:])
            self.dfs(s[1:],t)
        if s[0]!=t[0]:
            self.dfs(s[1:],t)