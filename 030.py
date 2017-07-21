class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        L = {}
        wordNum = len(words)
        for i in words:
            if i not in L:
                L[i] = 1
            else:
                L[i] += 1  #建立字典，统计
        wordLen=len(words[0])
        res=[]
        for i in range(len(s)+1-wordNum*wordLen):
            curr={}
            j=0
            while j<wordNum:
                word=s[i+j*wordLen:i+(j+1)*wordLen]
                if word not in L:
                    break
                if word not in curr:
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>L[word]:break
                j+=1
            if j==wordNum:res.append(i)
        return res
