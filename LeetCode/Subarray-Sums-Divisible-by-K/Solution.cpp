1#include <vector>
2#include <unordered_map>
3using namespace std;
4class Solution {
5public:
6    int subarraysDivByK(vector<int>& nums, int k) {
7        unordered_map <int,int> map;
8        map[0]=1;
9        int prefixsum=0;
10        int count=0;
11
12        for(int num:nums)
13        {
14            prefixsum += num;
15            int remainder = prefixsum % k;
16            if (remainder < 0)
17                remainder += k;
18            if (map.count(remainder))
19                count += map[remainder];
20            map[remainder]++;
21        }
22        return count;
23    }
24};