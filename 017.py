class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #DP问题 dp[n]=dp[n-1]*abc
        d = {'0': ' ', '1': '*', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv','9': 'wxyz'}
        ans=[]
        for i in digits:
            tmp=[]
            for j in d[i]:
                if len(ans)==0:
                    tmp.append(j)
                for k in ans:
                    tmp.append(k+j)
            ans=tmp
        return ans
