class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        ans=[]
        self.count=0
        def dfs(start,nums):
            if self.count==k:
                ans.append(nums)
                return
            for i in range(start,n+1)
                self.count+=1
                dfs(i+1,nums+[i])
                self.count-=1
        dfs(1,[])
        return ans
        使用dfs居然TLE了 改成递归
        """
        if k == 1:
            return [[i + 1] for i in range(n)]
        result = []
        if n > k:
            result = [r + [n] for r in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
        else:
            result = [r + [n] for r in self.combine(n - 1, k - 1)]
        return result