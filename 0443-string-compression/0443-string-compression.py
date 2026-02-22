class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("")
        ex = chars[0]
        cnt = 0
        p = 0
        for i in (chars):
            if i == ex:
                cnt += 1
            else:
                chars[p] = ex
                p += 1
                if cnt > 1:
                    for j in str(cnt):
                        chars[p] = j
                        p += 1
                    cnt = 1
                ex = i
        return p