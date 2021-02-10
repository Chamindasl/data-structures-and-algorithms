"""
[21-01-02] 841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)

        def dfs(room):
            if not visited[room]:
                visited[room] = True
                for next_room in rooms[room]:
                    dfs(next_room)
        
        dfs(0)
        
        for i in visited:
            if not i: return False
        
        
        return True
        
