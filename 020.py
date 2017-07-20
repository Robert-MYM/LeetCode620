class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' and stack:
                if (stack[-1]!='('):return False
                stack.pop()
            elif s[i]==']' and stack:
                if (stack[-1]!='['):return False
                stack.pop()
            elif s[i]=='}' and stack:
                if (stack[-1]!='{'):return False
                stack.pop()
            else:
                return False
        if stack:return False
        return True