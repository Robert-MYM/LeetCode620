class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #dp[n]='('+dp[i]+')+dp[n-i-1]
        ans=[]
        if (n==0):return ans
        if (n==1):return ['()']
        for i in range(0,n):
            tmp1=self.generateParenthesis(i)
            tmp2=self.generateParenthesis(n-1-i)
            for j in tmp1:
                for k in tmp2:
                    ans.append('('+j+')'+k)
                if len(tmp2)==0:
                    ans.append('('+j+')')
            if len(tmp1)==0:
                for k in tmp2:
                    ans.append('()'+k)
        return ans

