from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a = defaultdict(int)
        b = defaultdict(int)
        c = defaultdict(int)
        d = defaultdict(int)
        q = set()
        w = set()

        for i in range (len(word1)):
            a[word1[i]] += 1
            b[word2[i]] += 1
            q.add(word1[i])
            w.add(word2[i])

        for i in range (len(word1)):
            c[a[word1[i]]] += 1
            d[b[word2[i]]] += 1
        
        return q == w and c == d