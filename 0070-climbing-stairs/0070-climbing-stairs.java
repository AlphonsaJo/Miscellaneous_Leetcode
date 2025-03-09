
class Solution {


    
    public int climbStairs(int n) {
        
        if (n <= 0) return 0; // Invalid/Edge Case
        if (n == 1) return 1; // Base Case
        if (n == 2) return 2; // Two ways: One 2-steps or 2 1-steps

        int[] dp = new int[n+1];
        dp[0] = 1; // one way to stay at ground level
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];

    }
    
}