#coding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size=len(s)
        if s==1 :return s
        if s==2:
            if s[0]==s[1]:return s
            else: return s[0]
        max=1
        ans=s[0]
        i=0
        while i<size:
            j=i+1
            while j<size:   #合并一样的字符
                if s[i]==s[j]:j+=1
                else:break
            k=0
            while i-k-1>=0 and j+k<size:   #将s[i]作为中心点寻找回文
                if s[i-k-1]!=s[j+k]:break
                k+=1
            if (j-i+2*k)>max:
                max=j=i+2*k
                ans=s[i-k:j+k]
            if j+k==size-1:break
            i=j
        return ans

