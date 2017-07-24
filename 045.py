class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #i+nums[i]是以当前点为jump点能跳到的最远距离
        #对于决策来说，只要比较上一个最远距离是否能覆盖这个最远距离即可
        step=0
        maxdis=0
        last=maxdis
        for i in range(len(nums)):
            if i>last:
                last=maxdis
                step+=1
            maxdis=max(maxdis,i+nums[i])
        return step