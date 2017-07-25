class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        a = 0
        for i in range(len(nums) - 1):
            if a < i:
                return False
            a = max(a, i + nums[i])
            if a >= len(nums) - 1:
                return True
        return False
