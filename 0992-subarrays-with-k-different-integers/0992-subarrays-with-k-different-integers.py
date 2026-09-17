class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atmost(nums, k) - self.atmost(nums, k - 1)

    def atmost(self, nums, k):
        map = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            map[nums[right]] = map.get(nums[right], 0) + 1

            while len(map) > k:
                map[nums[left]] -= 1

                if map[nums[left]] == 0:
                    del map[nums[left]]

                left += 1

            count += right - left + 1

        return count
