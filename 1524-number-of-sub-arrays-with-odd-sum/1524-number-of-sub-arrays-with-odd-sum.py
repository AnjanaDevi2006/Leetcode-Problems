class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # dp to track counts for even and odd sum subarrays
        dp = [[0, 0], [0, 0]]

        # Stores the final count of subarrays with an odd sum
        count = dp[1][0]

        for i in range(n):
            # Alternates between 0 and 1 for even/odd index tracking
            idx = i & 1
            # Determines if the current element is odd (1) or even (0)
            parity = arr[i] & 1
            
            # If the current element is odd, it contributes to odd subarrays
            # If the current element is even, it contributes to even subarrays
            dp[parity][idx] = (1 + dp[0][1 - idx]) % MOD
            dp[1 - parity][idx] = dp[1][1 - idx] % MOD
            
            # Accumulate the count of odd subarrays
            count = (count + dp[1][idx]) % MOD

        return count