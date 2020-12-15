def grid_traveler(m, n, memo={}):
    mm, nn = min(m, n), max(m, n)
    key = str(mm) + "_" + str(nn)
    if key in memo: return memo[key]
    if m == 1 or n == 1: return 1
    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]

print(grid_traveler(475, 475))
