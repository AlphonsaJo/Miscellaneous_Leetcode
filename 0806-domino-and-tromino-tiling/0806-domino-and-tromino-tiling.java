class Solution {
    public int numTilings(int n) {
        int MOD = 1_000_000_007;

        // Handle base cases
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;

        // dp[i] will store the number of ways to tile a 2 x i board
        long[] dp = new long[n + 1];
        dp[0] = 1;  // Empty board
        dp[1] = 1;  // Only 1 vertical domino
        dp[2] = 2;  // Two vertical or two horizontal dominoes

        for (int i = 3; i <= n; i++) {
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD;
        }

        return (int) dp[n];
    }
}
