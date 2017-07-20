class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:return s
        ans=""
        ls=len(s)
        num=(numRows-1)*2
        for i in range(1,numRows+1):
            k=i-1
            while k<ls:
                ans+=s[k]
                if i!=1 and i!=numRows and (numRows-i)*2+k<ls :
                    ans+=s[(numRows-i)*2+k]
                k+=num
        return ans
