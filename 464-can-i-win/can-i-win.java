class Solution {

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
       
        if (desiredTotal == 0) return true;
        
        int sum = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
    
        if (sum < desiredTotal) return false;
       
        Boolean[] memo = new Boolean[1 << maxChoosableInteger];
        
        return dfs(maxChoosableInteger, desiredTotal, 0, memo);
    }
    
    private boolean dfs(int max, int target, int mask, Boolean[] memo) {
        
        if (memo[mask] != null) return memo[mask];
        
        for (int i = 1; i <= max; i++) {
            
            int bit = 1 << (i - 1);
            
            if ((mask & bit) == 0) {
            
                if (i >= target || 
                    !dfs(max, target - i, mask | bit, memo)) {
                    
                    return memo[mask] = true;
                }
            }
        }
        
        return memo[mask] = false;
    }
}