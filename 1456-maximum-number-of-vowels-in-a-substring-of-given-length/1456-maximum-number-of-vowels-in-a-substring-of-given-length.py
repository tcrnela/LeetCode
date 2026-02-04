from collections import deque

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        q = deque()
        ans = 0
        cur = 0
        for i in range (len(s)):
            if len(q) >= k:
                if q[0] in vowels: cur -= 1
                q.popleft()

            if s[i] in vowels:
                cur += 1
                if ans < cur: ans = cur
            q.append(s[i])
            
        return ans