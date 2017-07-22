class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #第10题变种但是TLE放弃重写
        if len(p) == 0: return len(s) == 0
        for i in range(len(p)):
            if p[i] != '*': break
            if i == len(p) - 1: return True
        if len(s) == 0: return False
        if p[0] == '?' or p[0] == s[0]: return self.isMatch(s[1:], p[1:])
        if p[0] == '*': return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])#<--估计是这步的问题，寻求一个线性搜索方案比较好
        return False