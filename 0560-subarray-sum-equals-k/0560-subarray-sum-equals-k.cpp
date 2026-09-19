#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        mp[0]=1;
        int prefixsum=0;
        int count=0;
        for(int num:nums)
        {
            prefixsum += num;
            if(mp.find(prefixsum - k)!= mp.end()){
                count +=mp[prefixsum - k];
            }
            mp[prefixsum]++;
        }
        return count;
    }
};