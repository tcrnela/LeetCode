from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = True
        b = defaultdict(int)
        for i in range (len(magazine)):
            b[magazine[i]] += 1
        for i in range (len(ransomNote)):
            b[ransomNote[i]] -= 1
            if b[ransomNote[i]] < 0:
                ans = False
        return ans