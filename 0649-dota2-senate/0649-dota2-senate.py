from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        radi = 0
        dire = 0
        while (1):
            q.clear()
            for i in senate:
                if i == "R":
                    if dire > 0:
                        dire -= 1
                    else:
                        q.append(i)
                        radi += 1
                if i == "D":
                    if radi > 0:
                        radi -= 1
                    else:
                        q.append(i)
                        dire += 1
            senate = "".join(q)

            if "R" not in senate:
                return "Dire"
            elif "D" not in senate:
                return "Radiant"