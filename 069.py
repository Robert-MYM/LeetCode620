class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分
        if x == 0: return 0
        if x == 1: return 1
        up = x
        low = 0
        while up != low:
            res = (up + low) / 2
            if res == low: return low
            if res * res == x:
                return res
            elif res * res > x:
                up = res
            else:
                low = res
        return up

