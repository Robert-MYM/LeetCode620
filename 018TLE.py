class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #TLE算法,建立在3sum基础上的4sum,不知怎么优化，换用别的算法
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if(i-1>=0):
                if(nums[i]==nums[i-1]):continue
            tar=target-nums[i]
            tmp=self.threeSum(nums[i+1:],tar)
            for j in range(len(tmp)):
                tmp[j].insert(0,nums[i])
                res.append(tmp[j])
        return res

    def threeSum(self, nums,target):
        #nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1;
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == target-nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1;
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                    elif nums[left] + nums[right] < target-nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]: break
                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]: break
        return res