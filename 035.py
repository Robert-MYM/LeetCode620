class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #二分again
        if len(nums) == 0: return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if start == end:
                if target > nums[mid]:
                    return mid + 1
                elif target < nums[mid]:
                    return mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start
