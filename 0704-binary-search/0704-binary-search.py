class Solution:

    def binary_search(self,Array,start,end,target):
        if start > end:
            return -1
        mid = (start + end )//2

        if Array[mid] == target:
            return mid
        elif Array[mid] < target:
            return self.binary_search(Array,mid+1,end,target)
        else:
            return self.binary_search(Array,start,mid-1,target)
 
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        ans = self.binary_search(nums,start,end,target)
        return ans

        