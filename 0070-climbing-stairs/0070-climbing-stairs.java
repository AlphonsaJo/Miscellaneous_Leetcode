class Solution {
    public int climbStairs(int n) {
        //initialize size (n+1) to include dp[n]
        int dp[] = new int[n+1];

        //handle edge cases
        if(n<=1)
            return 1;

        //base cases
        dp[0] = 1;
        dp[1] = 1;

        // Bottom-up DP computation
        for(int i=2; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }

        //store and return result
        int result = dp[n];
        return result;
    }
}