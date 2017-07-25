class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #写了几次，始终有问题，改完之后的程序绕的越来越复杂，参考别人的解法，学习了有穷状态自动机（DFA）的解法，觉得最是优雅
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EXPONENT = 5
        # 0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable = [[-1, 0, 3, 1, 2, -1],  # 0 no input or just spaces
                           [-1, 8, -1, 1, 4, 5],  # 1 input is digits
                           [-1, -1, -1, 4, -1, -1],  # 2 no digits in front just Dot
                           [-1, -1, -1, 1, 2, -1],  # 3 sign
                           [-1, 8, -1, 4, -1, 5],  # 4 digits and dot in front
                           [-1, -1, 6, 7, -1, -1],  # 5 input 'e' or 'E'
                           [-1, -1, -1, 7, -1, -1],  # 6 after 'e' input sign
                           [-1, 8, -1, 7, -1, -1],  # 7 after 'e' input digits
                           [-1, 8, -1, -1, -1, -1]]  # 8 after valid input input space
        state=0 #状态初始为0
        for i in s:
            inputtype=INVALID
            if i==' ':inputtype=SPACE
            elif i in '1234567890':inputtype=DIGIT
            elif i=='-' or i=='+':inputtype=SIGN
            elif i=='.':inputtype=DOT
            elif i=='e' or i=='E':inputtype=EXPONENT
            state=transitionTable[state][inputtype]
            if state==-1:return False
        return state==1 or state==4 or state==7 or state==8
