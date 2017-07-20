class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #学习了一下罗马数字的组成
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        list = ''
        for i in range(0, len(value)):
            while num >= value[i]:
                num -= value[i]
                list += sym[i]
        return list