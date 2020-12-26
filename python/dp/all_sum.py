def allSumMemo(candidates: List[int], target: int, memo={}):
    if target in memo: return memo[target]
    if target == 0: return [[]]
    if target < 0: return []
    re = []
    for i in range(len(candidates)):
        re += [one + [candidates[i]] for one in allSumMemo(candidates, target - candidates[i], memo)]
    memo[target] = re
    return memo[target]


def allSumDpArray(candidates: List[int], target: int):
    dp = [None] * (target + 1)
    for i in range(len(dp)):
        dp[i] = []
    dp[0] = [[]]
    for i in range(target + 1):
        if dp[i]:
            for j in candidates:
                if i + j <= target:
                    dp[i + j] += [one + [j] for one in dp[i]]
    return dp[target]


# print(allSumMemo([2,3,4], 6))
# print(allSumDpArray([2,3,4], 6))
print(allSumMemo([7, 14], 300))
print(allSumDpArray([7, 14], 300))
