class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=float('-inf')
        currsum=0
        for i in nums:
            currsum+=i
            maxsum=max(maxsum,currsum)
            if currsum<0:
                currsum=0
        return maxsum