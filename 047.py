class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        Solution.ls=len(nums)
        sub=[]
        Solution.res=[]
        self.dfs(nums,sub)
        return Solution.res

    def dfs(self,nums,sublist):
        if len(sublist)==Solution.ls:
            #if sublist[:] not in Solution.res:  这里如果用in方法的话 会TLE
            Solution.res.append(sublist[:])
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:continue
            tmp=nums[i]
            del nums[i]
            sublist.append(tmp)
            self.dfs(nums,sublist)
            sublist.pop()
            nums.insert(i,tmp)