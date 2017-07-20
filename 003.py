class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        maxlen=0
        dict={}
        for i in range(len(s)):
            dict[s[i]]=-1
        for i in range(len(s)):
            if dict[s[i]]!=-1:
                while start<=dict[s[i]]:  #遇到重复后循环将之前的从字典中取出
                    dict[s[start]]=-1
                    start+=1
            if i-start+1>maxlen:maxlen=i-start+1
            dict[s[i]]=i
        return maxlen
