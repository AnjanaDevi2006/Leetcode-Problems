1class Solution {
2public:
3    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
4        int n=nums.size();
5        vector<int> result(n-k+1);
6        deque<int> d;
7        for(int right=0;right<n;right++){
8            while(!d.empty()&&d.front()<=right-k){
9                d.pop_front();
10            }
11            while(!d.empty() && nums[d.back()]<nums[right]){
12                d.pop_back();
13            }
14            d.push_back(right);
15            if (right>=k-1){
16                result[right-k+1]=nums[d.front()];
17            }
18        }
19        return result;
20    }
21};