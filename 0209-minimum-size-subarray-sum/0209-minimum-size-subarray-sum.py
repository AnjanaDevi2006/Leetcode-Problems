class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        s=0
        minlen=float('inf')
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                minlen=min(minlen,right-left+1)
                s-=nums[left]
                left+=1
        return 0 if minlen==float('inf') else minlen