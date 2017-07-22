class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #难度不大，木桶原理，搜索左右最高点 取低的
        n=len(height)
        leftmost = [0 for i in range(n)]
        left=0
        for i in range(n):
            if height[i]>left:left=height[i]
            leftmost[i]=left
        res=0
        right=0
        for i in reversed(range(n)):
            if height[i]>right:right=height[i]
            if min(right,leftmost[i])>height[i]:
                res+=min(right,leftmost[i])-height[i]
        return res

