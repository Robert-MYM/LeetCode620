class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[3,4,-1,1] return 2.
        #灵活运用数组的index属性
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:nums[i]=n+2
        for i in range(n):   #题目里会出现2个1这种情况，需要用abs约束一下翻转
            if abs(nums[i])<=n:
                curr=abs(nums[i])-1
                nums[curr]=-abs(nums[curr])
        for i in range(n):
            if nums[i]>0:return i+1
        return n+1