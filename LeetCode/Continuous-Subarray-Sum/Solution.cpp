1#include <unordered_map>
2using namespace std;
3class Solution {
4public:
5    bool checkSubarraySum(vector<int>& nums, int k) {
6        unordered_map<int,int> map;
7        map[0]=-1;
8        int prefixsum=0;
9        for(int i=0;i<nums.size();i++)
10        {
11          prefixsum += nums[i];
12          int rem = prefixsum % k;
13           if(map.find(rem)!= map.end()){
14                if (i-map[rem]>=2){
15                    return true;
16                }
17            }
18            else
19            {
20                map[rem]=i;
21            }
22        }
23        return false;
24        }
25        
26};