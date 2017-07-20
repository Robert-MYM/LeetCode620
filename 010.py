class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #递归
        #当p[i]!='*' 则匹配p[i-1]==s[i-1](注意'.'强制算相等） 成功则继续匹配p[i]与s[i]
        #当p[i]=='*' 则匹配p[i-1]==s[i-1](注意'.'强制算相等） 成功则继续匹配p[i]与s[i+1]或者p[i-1]与s[i+1]
        if len(p)==0:return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1
            ls=len(s)
            while i<ls and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]):return True
                i+=1
            return False
