class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #对subsetI稍作改动，添加字典判断是否重复，因为字典要用tuple，为了避免1，2和2，1的作为list重复但作为tuple不重复的情况，要先将nums排序
        res = [[]]
        nums.sort()
        dict = {}
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                if tuple(x) not in dict:
                    res.append(x)
                    dict[tuple(x)] = 1
        return res