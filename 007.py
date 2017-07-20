class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        v=x
        flag=1
        if v<0:
            flag=-1
            v=-v
        res=0
        while v!=0:
            res=res*10+v%10
            v=v/10
        res=res*flag
        if (res>((2**31)-1)) or (res<(-(2**31))):return 0
        else:return res
