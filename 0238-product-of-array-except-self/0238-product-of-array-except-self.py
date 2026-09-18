class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        ans[0]=1
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        rightprod=1
        for i in range(n-1,-1,-1):
            ans[i]*=rightprod
            rightprod*=nums[i]
        return ans