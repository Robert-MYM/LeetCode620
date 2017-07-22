class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #递归
        if n==1:return '1'
        tmp=self.countAndSay(n-1)
        res=''
        count=0
        k=tmp[0]
        for i in tmp:
            if (k==i):count+=1
            else:
                res=res+str(count)+k
                k=i
                count=1
        return res


