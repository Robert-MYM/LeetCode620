class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #这种题用python就很好做
        if len(nums) == 0: return 0
        if len(nums) == 1 and nums[0]!=val: return 1
        if len(nums) == 1 and nums[0] == val: return 0
        i = 0
        while 1:
            if i >= len(nums): break
            if val == nums[i]:
                del nums[i]
                i -= 1
            i += 1
        return len(nums)