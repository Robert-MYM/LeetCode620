class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        res=[]
        for i in strs:
            tmp=''.join(sorted(i))
            if tmp in dict:
                dict[tmp]+=[i]
            else:
                dict[tmp]=[i]
        for i in dict:
            tmp=dict[i]
            #tmp.sort()
            res+=[tmp]
        return res
