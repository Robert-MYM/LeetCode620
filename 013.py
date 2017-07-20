class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #罗马数字组成很有意思，看起来会有CD，IV这种特殊的双元组合，但是你在one by one的分析的时候也是可以solve这种组合的
        res=self.onenum(s[0])
        for i in range(1,len(s)):
            if self.onenum(s[i-1])<self.onenum(s[i]):
                res+=self.onenum(s[i])-2*self.onenum(s[i-1])
            else:
                res+=self.onenum(s[i])
        return res

    def onenum(self,c):
        if (c=='I'):return 1
        if (c == 'V'): return 5
        if (c == 'X'): return 10
        if (c == 'L'): return 50
        if (c == 'C'): return 100
        if (c == 'D'): return 500
        if (c == 'M'): return 1000
        return 0

