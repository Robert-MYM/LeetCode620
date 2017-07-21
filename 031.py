class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:return
        ls=len(nums)-2
        while ls>=0 and nums[ls]>=nums[ls+1]: ls-=1
        if ls>=0:
            i=ls+1
            while i<len(nums) and nums[i]>nums[ls]:i+=1
            nums[i-1],nums[ls]=nums[ls],nums[i-1]
        #nums[ls+1:].reverse() py的reverse是倒序不是翻转list
        left, right = ls + 1, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1