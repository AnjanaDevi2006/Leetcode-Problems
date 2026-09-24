1class Solution {
2public:
3    int maxProduct(vector<int>& nums) {
4        int prefix=1;
5        int suffix=1;
6        int ans= INT_MIN;
7        int n=nums.size();
8        for(int i=0;i<n;i++){
9            if (prefix==0) prefix=1;
10            if (suffix==0) suffix=1;
11            prefix *= nums[i];
12            suffix *= nums[n-1-i];
13            ans=max(ans,max(prefix,suffix));
14        }
15        return ans;
16    }
17};