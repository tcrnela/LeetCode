from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)
        for i in arr:
            a[i] += 1
        for i in a:
            if b[a[i]] > 0: return False
            b[a[i]] += 1
        return True