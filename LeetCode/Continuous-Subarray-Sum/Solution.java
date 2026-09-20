1class Solution {
2    public boolean checkSubarraySum(int[] nums, int k) {
3        Map<Integer,Integer> map=new HashMap<>();
4        map.put(0,-1);
5        int prefixsum=0;
6        for(int i=0;i<nums.length;i++){
7            prefixsum += nums[i];
8            int rem=prefixsum % k;
9            if(map.containsKey(rem)){
10                if (i-map.get(rem)>=2){
11                    return true;
12                }
13            }
14            else
15            {
16                map.put(rem,i);
17            }
18        }
19        return false;
20    }
21}