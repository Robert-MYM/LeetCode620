class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        if n==0:return 0
        max1=0
        height=[0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:height[j]=0
            tmp=self.largestRectangleArea(height)
            if tmp>max1:max1=tmp
        return max1


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #来自博客toplatona的栈解法
        maxArea = 0
        stack = []
        i = 0
        while i < len(heights):
            if len(stack) == 0 or stack[-1] <= heights[i]:
                stack.append(heights[i])
            else:
                count = 0
                while len(stack) > 0 and stack[-1] > heights[i]:
                    count += 1
                    maxArea = max(maxArea, stack[-1] * count)
                    stack.pop()
                while count > 0:
                    count -= 1
                    stack.append(heights[i])
                stack.append(heights[i])
            i += 1
        count = 1
        while len(stack) != 0:
            maxArea = max(maxArea, stack[-1] * count)
            stack.pop()
            count += 1
        return maxArea


