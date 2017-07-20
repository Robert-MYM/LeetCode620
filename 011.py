class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #O(n)
        i=0
        j=len(height)-1
        maxx=0
        while (i!=j):
            if (height[i]<=height[j]):
                if (maxx<height[i]*(j-i)):
                    maxx=height[i]*(j-i)
                i+=1
            else:
                if (maxx<height[j]*(j-i)):
                    maxx=height[j]*(j-i)
                j-=1
        return maxx
