class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirst(nums, target), self.findLast(nums, target)]

    def findFirst(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def findLast(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
