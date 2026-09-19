class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixsum=0
        count = 0
        freq = {0:1}
        
        for num in nums:
            prefixsum +=num

            if prefixsum-k in freq:
                count += freq[prefixsum-k]
                
            freq[prefixsum] = freq.get(prefixsum,0)+1
        return count