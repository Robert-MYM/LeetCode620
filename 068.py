class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #需要先去判断能装多少个word，再去考虑空格
        ans = []
        i = 0
        while i < len(words):
            size, begin = 0, i
            while i < len(words):
                if size == 0:
                    newsize = len(words[i])
                else:
                    newsize = size + len(words[i]) + 1
                if newsize <= maxWidth:
                    size = newsize
                else:
                    break
                i += 1
            s = maxWidth - size
            if i - begin - 1 > 0 and i < len(words):
                ns = s / (i - begin - 1)
                s %= i - begin - 1
            else:
                ns = 0
            j = begin
            while j < i:
                if j == begin:
                    tmp = words[j]
                else:
                    tmp += ' ' * (ns + 1)
                    if s > 0 and i < len(words):
                        tmp += ' '
                        s -= 1
                    tmp += words[j]
                j += 1
            tmp += ' ' * s
            ans.append(tmp)
        return ans


