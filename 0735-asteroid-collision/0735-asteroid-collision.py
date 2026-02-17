class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in asteroids:
            if i < 0:
                f = 1
                while(stk and stk[-1] > 0):
                    if stk[-1] > abs(i):
                        f = 0
                        break
                    elif stk[-1] == abs(i):
                        stk.pop()
                        f = 0
                        break
                    else:
                        stk.pop()
                if f:
                    stk.append(i)
            else:
                stk.append(i)
        return stk