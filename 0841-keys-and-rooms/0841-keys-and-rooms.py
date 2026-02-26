class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(n):
            visited.add(n)
            for i in rooms[n]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited) == len(rooms)
                