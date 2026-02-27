from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        ans = float("inf")
        vis = set()
        q = deque()
        flag = 0

        r = ["+"] * (len(maze[0]) + 2)
        maze = [r] + [["+"] + row + ["+"] for row in maze] + [r]
        entrance[0] += 1
        entrance[1] += 1
        
        q.append((entrance[0], entrance[1], 0))
        vis.add(tuple(entrance))

        while(q):
            (y, x, z) = q.popleft()
            if (y, x) != tuple(entrance) and (y == 1 or y == len(maze) - 2 or x == 1 or x == len(maze[0]) - 2):
                if ans > z:
                    ans = z
                    flag = 1
            for i in range (4):
                if maze[y + dy[i]][x + dx[i]] == "." and (y + dy[i], x + dx[i]) not in vis:
                    vis.add((y + dy[i], x + dx[i]))
                    q.append((y + dy[i], x + dx[i], z + 1))
        if flag == 0: return -1
        return ans