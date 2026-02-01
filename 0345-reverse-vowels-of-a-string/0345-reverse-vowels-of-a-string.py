class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        ans = []
        for i in range (len(s)):
            if s[i] == "A" or s[i] == "a" or s[i] == "E" or s[i] == "e" or s[i] == "I" or s[i] == "i" or s[i] == "O" or s[i] == "o" or s[i] == "U" or s[i] == "u":
                vowels.append(s[i])
        for i in range (len(s)):
            if s[i] == "A" or s[i] == "a" or s[i] == "E" or s[i] == "e" or s[i] == "I" or s[i] == "i" or s[i] == "O" or s[i] == "o" or s[i] == "U" or s[i] == "u":
                ans.append(vowels.pop())
            else:
                ans.append(s[i])
        return "".join(ans)