class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #a=[-2,1,-2,4,3,5,6,1,5]
        #b=[-2,1,1,4,4,5,6,6,6]
        if len(nums)==1:return nums[0]
        a=b=nums[0]
        for i in range(1,len(nums)):
            a=max(nums[i],a+nums[i])  #以nums[i]结束的最大array，要么是nums[i]本身，要么是nums[i]+maxarray[nums[i-1]
            b=max(a,b)  #
        return b