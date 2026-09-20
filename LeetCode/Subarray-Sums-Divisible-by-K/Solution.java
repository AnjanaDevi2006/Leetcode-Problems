1class Solution {
2    public int subarraysDivByK(int[] nums, int k) {
3        HashMap <Integer,Integer> map = new HashMap<>();
4        int count=0;
5        int prefixsum=0;
6        map.put(0,1);
7
8        for(int num:nums){
9            prefixsum +=num;
10            int remainder = prefixsum % k;
11            if (remainder < 0)
12            {
13                remainder += k;
14            }
15            if (map.containsKey(remainder))
16            {
17                count +=map.get(remainder);
18            }
19            map.put(remainder,map.getOrDefault(remainder,0)+1);
20        }
21        return count;
22    }
23}