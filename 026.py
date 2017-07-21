class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        i = 1
        while 1:
            if i >= len(nums): break
            if nums[i - 1] == nums[i]:
                del nums[i]
                i -= 1
            i += 1
        return len(nums)