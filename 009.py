class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #计算反转后是否相等
        if(x<0):return False
        res=0
        v=x
        while v!=0:
            res=res*10+v%10
            v=v/10
        return res==x