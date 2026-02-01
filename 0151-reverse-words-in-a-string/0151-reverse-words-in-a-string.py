class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        a = s.split()
        b = ""
        for i in range (len(a)-1, 0, -1):
            b += a[i] 
            b += " "
        b += a[0]
        return b