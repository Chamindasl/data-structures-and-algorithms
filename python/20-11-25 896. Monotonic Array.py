# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0]<A[-1]:
            prev = A[0]
            for a in A:
                if prev > a:
                    return False
                prev = a
        else:
            prev = A[0]
            for a in A:
                if prev < a:
                    return False
                prev = a
        return True
