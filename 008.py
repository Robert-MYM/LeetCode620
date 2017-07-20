class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        k = 0
        flag = 1
        ls = len(str)
        while (k < ls) and (str[k] == ' '): k += 1
        if (k < ls) and (str[k] == '+'):
            flag = 1
            k += 1
        elif (k < ls) and (str[k] == '-'):
            flag = -1
            k += 1
        else:
            flag = 1
        while (k < ls) and str[k] >= '0' and str[k] <= '9':
            res = res * 10 + ord(str[k]) - 48
            k += 1
        res = res * flag
        if (res > ((2 ** 31) - 1)):
            return ((2 ** 31) - 1)
        elif (res < (-(2 ** 31))):
            return (-(2 ** 31))
        else:
            return res

