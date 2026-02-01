from collections import deque

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        b = len(word1) if len(word1) <= len(word2) else len(word2)
        c1 = c2 = 0

        for i in range (b*2):
            if i % 2 == 0:
                a.append(word1[c1])
                c1 += 1
            else:
                a.append(word2[c2])
                c2 += 1

        if c1 < len(word1):
            for i in range (c1, len(word1)):
                a.append(word1[i])
        elif c2 < len(word2):
            for i in range (c2, len(word2)):
                a.append(word2[i])

        a = "".join(a)
        return a