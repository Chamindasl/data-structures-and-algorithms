"""
[21-01-04] 784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        re = []
        def backtrack(i, comb):
            if len(comb) == len(S):
                re.append(comb)
                return
            if S[i].isalpha():
                backtrack(i+1, comb+S[i].lower())
                backtrack(i+1, comb+S[i].upper())
            else:
                backtrack(i+1, comb+S[i])
        
        def premutationWay():
            result = []
            result.append(S.lower())
            for i in range(len(S)):
                size = len(result)
                for j in range(size):
                    if S[i].isalpha():
                        result.append(result[j][:i]+ S[i].upper() + result[j][i+1:])

            return result

        return premutationWay()

        # backtrack(0, '')
        # return re

