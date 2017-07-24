class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub=[]
        Solution.res=[]
        self.dfs(nums,sub)
        return Solution.res

    def dfs(self,nums,sublist):
        if len(nums)==len(sublist):
            Solution.res.append(sublist[:])
            return
        for i in nums:
            if i in sublist:continue#去除重复元素
            sublist.append(i)
            self.dfs(nums,sublist)
            sublist.remove(i)

