def fib_dp_memo(n, memo={0: 0, 1: 1}):
    if n in memo: return memo[n]
    fib = fib_dp_memo(n - 1, memo) + fib_dp_memo(n - 2, memo)
    memo[n] = fib
    return memo[n]
print(fib_dp_memo(50))
