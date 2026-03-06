class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in s:
            stk.append(i)
            if i == "]":
                stk.pop()
                cur = ""
                while stk[-1] != "[":
                    cur = stk.pop() + cur
                stk.pop()
                num = ""
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(cur * int(num))
        return "".join(stk)