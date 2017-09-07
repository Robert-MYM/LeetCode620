class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #考察gray码的一种快速定义，右移异或可得当前位gray码！
        res = []
        for i in range(2 ** n):
            g =(i>>1)^i
            res.append(g)
        return res