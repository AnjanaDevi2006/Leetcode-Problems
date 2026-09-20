1class Solution:
2    def subarraysDivByK(self, nums: list[int], k: int) -> int:
3        remainder_count={0:1}
4        prefixsum=0
5        count=0
6        for num in nums:
7            prefixsum += num
8            remainder = prefixsum % k
9            if remainder < 0:
10                remainder += k
11            if remainder in remainder_count:
12                count += remainder_count[remainder]
13            remainder_count[remainder] = remainder_count.get(remainder,0)+1
14        return count