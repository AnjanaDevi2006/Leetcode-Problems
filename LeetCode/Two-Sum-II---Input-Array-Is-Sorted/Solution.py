1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        n=len(numbers)
4        left=0
5        right=n-1
6        while left<right:
7            sum=numbers[left]+numbers[right]
8            if sum==target:
9                return (left+1,right+1)
10            elif sum>target:
11                right-=1
12            else:
13                left+=1
14        return [-1,-1]