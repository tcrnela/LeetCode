from collections import deque

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        q = deque()
        ans = 0
        cur = 0
        l = 0
        r = 0
        while (r < len(s)):
            if s[r] in vowels:
                cur += 1
            if cur > ans: ans = cur
            r += 1
            if r - l >= k:
                if s[l] in vowels:
                    cur -= 1
                l += 1

        return ans