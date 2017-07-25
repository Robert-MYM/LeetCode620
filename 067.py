class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        if len(b) > len(a):
            a, b = b, a
        la = len(a) - 1
        lb = len(b) - 1
        jin = 0
        while la >= 0:
            if lb >= 0:
                if a[la] == '0' and b[lb] == '0':
                    res += str(jin);jin = 0
                elif a[la] == '1' and b[lb] == '0' and jin == 0:
                    res += '1'
                elif a[la] == '1' and b[lb] == '0' and jin == 1:
                    res += '0'
                elif a[la] == '0' and b[lb] == '1' and jin == 0:
                    res += '1';
                elif a[la] == '0' and b[lb] == '1' and jin == 1:
                    res += '0'
                elif a[la] == '1' and b[lb] == '1' and jin == 0:
                    res += '0';jin = 1
                elif a[la] == '1' and b[lb] == '1' and jin == 1:
                    res += '1'
            else:
                if a[la] == '0' and jin == 0:
                    res += '0'
                elif a[la] == '0' and jin == 1:
                    res += '1';jin = 0
                elif a[la] == '1' and jin == 0:
                    res += '1'
                elif a[la] == '1' and jin == 1:
                    res += '0'
            la -= 1
            lb -= 1
        if jin == 1: res += '1'
        return res[::-1]
