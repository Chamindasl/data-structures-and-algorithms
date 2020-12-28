"""
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remain, count, next_start):
            if remain < 0 or count > k: return []
            if remain == 0 and count == k:
                # results.append(list(comb))
                return [[]]
            results = []
            for i in range(next_start, 10):
                results += [[i] + one for one in backtrack(remain - i, count + 1, i + 1)]
            
            return results
            
        return backtrack(n, 0, 1)

