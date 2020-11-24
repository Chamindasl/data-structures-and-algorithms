// 509. Fibonacci Number
class Solution {
    public int fib(int N) {
        if (N == 0) return 0;
        if (N == 1) return 1;
        int fib_n_1 = 1, fib_n_2 = 0;
        int fib_n = 0;
        for (int i = 2; i<=N; i++) {
            fib_n = fib_n_1 + fib_n_2;
            fib_n_2 = fib_n_1;
            fib_n_1 = fib_n;
        }
        return fib_n;
    }
}
