class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxx=0;
        int maxtemp=0;
        for(int i =0;i<nums.size();++i){
           if(nums[i]==1) maxtemp++;
           else maxx=max(maxx,maxtemp),maxtemp=0;     
        }
        return max(maxx,maxtemp);
    }
};