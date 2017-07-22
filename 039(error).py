class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(candidates) == 0: return res
        for i in range(len(candidates)):
            if target > candidates[i]:
                tmp = self.combinationSum(candidates[i:], target - candidates[i])
                if len(tmp) != 0:
                    for j in tmp:
                        res.append(j.append(candidates[i]))
            elif target == candidates[i]:
                res.append([candidates[i]])
            else:
                return res
        return res
