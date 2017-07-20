import collections
import itertools

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #先两两求和，放入索引，再计算后笛卡儿积一下
        two_sum = collections.defaultdict(list)
        ret = set()
        for (id1, val1), (id2, val2) in itertools.combinations(enumerate(nums), 2):
            two_sum[val1 + val2].append({id1, id2})
        keys = two_sum.keys()
        for key in keys:
            if two_sum[key] and two_sum[target - key]:
                for pair1 in two_sum[key]:
                    for pair2 in two_sum[target - key]:
                        if pair1.isdisjoint(pair2):
                            ret.add(tuple(sorted([nums[i] for i in pair1 | pair2])))
                del two_sum[key]
                if key != target - key:
                    del two_sum[target - key]
        return [list(i) for i in ret]