1class Solution {
2    public int maxProduct(int[] nums) {
3        int prefix=1;
4        int suffix=1;
5        int ans= Integer.MIN_VALUE;
6        int n=nums.length;
7        for(int i=0;i<n;i++){
8            if (prefix==0) prefix=1;
9            if (suffix==0) suffix=1;
10            prefix *= nums[i];
11            suffix *= nums[n-1-i];
12            ans=Math.max(ans,Math.max(prefix,suffix));
13        }
14        return ans;
15    }
16}