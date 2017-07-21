class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:return 0
        if len(s)==1:return 0
        maxlen=0
        tmp=-1
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':stack.append(i)  #core 储存左括号的下标
            else:
                if not stack:tmp=i
                else:
                    stack.pop()
                    if not stack:
                        maxlen=max(maxlen,i-tmp)
                    else:
                        maxlen=max(maxlen,i-stack[-1])
        return maxlen
