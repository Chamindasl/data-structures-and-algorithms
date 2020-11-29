# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
    
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p : p[0]**2 + p[1]**2)
        return points[:K]
        
