class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:return ""
        str=strs[0]
        minn=len(str)
        for i in range(1,len(strs)):
            j=0
            tmp=strs[i]
            while j<minn and j<len(tmp) and tmp[j]==str[j]:j+=1
            minn=j
        return str[:minn]
