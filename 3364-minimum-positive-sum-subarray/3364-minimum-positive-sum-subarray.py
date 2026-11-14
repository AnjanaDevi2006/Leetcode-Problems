class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """

        n = len(nums)
        min_sum = float('inf')
    
        # Check all valid subarray sizes between l and r
        for size in range(l, r + 1):
            if size > n:
                continue
            
            # Calculate the sum of the first window of this size
            current_window_sum = sum(nums[:size])
            if current_window_sum > 0:
                min_sum = min(min_sum, current_window_sum)
            
        # Slide the window across the rest of the array
            for i in range(size, n):
                current_window_sum += nums[i] - nums[i - size]
                if current_window_sum > 0:
                    min_sum = min(min_sum, current_window_sum)
                
        return min_sum if min_sum != float('inf') else -1
        