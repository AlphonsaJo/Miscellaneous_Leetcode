class Solution {
    public int fib(int n) {
        // Bottom-up dp (tabulation) approach
        // not optimized for space
        int[] dp = new int[n+1];

        if(n==0){
            return 0;
        }

        if(n<3){
            return 1;
        }

        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }

        int result = dp[n];
        return result;
    }
}