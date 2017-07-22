class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ret=[]
        self.dfs(candidates,target,[])
        return Solution.ret
    def dfs(self,candidates,target,valuelist):
        if target==0:
            Solution.ret.append(valuelist)
        for i in range(len(candidates)):
            if target<candidates[i]:return
            self.dfs(candidates[i:],target-candidates[i],valuelist+[candidates[i]])
