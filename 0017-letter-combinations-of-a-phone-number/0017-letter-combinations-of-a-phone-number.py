class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # 1. 종료 조건: 입력된 숫자 길이만큼 다 채웠을 때
            if len(path) == len(digits):
                res.append(path)
                return
            
            # 2. 현재 숫자에서 가능한 문자들을 하나씩 순회
            current_digit = digits[index]
            for letter in phone[current_digit]:
                # 3. 다음 숫자로 넘어가기 (재귀 호출)
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return res