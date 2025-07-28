class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int dp[] = new int[n+1];

        dp[0] = cost[0];
        dp[1] = cost[1];
        int minSteps = 0;

        for(int i = 2; i<n; i++){
            minSteps = Math.min(dp[i-1], dp[i-2]);
            dp[i] = cost[i] + minSteps;
        }

        return Math.min(dp[n - 1], dp[n - 2]); // min cost to reach top floor 
                                               // so n not i
    }
}