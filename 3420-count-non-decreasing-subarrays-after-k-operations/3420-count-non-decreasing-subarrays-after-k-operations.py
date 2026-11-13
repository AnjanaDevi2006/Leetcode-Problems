class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        right = len(nums) - 1
        total_cost = 0
        q = deque() # reqval, count
        res = 0

        for left in range(len(nums)-1, -1, -1):
            x = nums[left]
            c = 1

            while q and q[0][0] < x:
                value, count = q.popleft()    
                total_cost += (x - value) * count
                c += count
            
            q.appendleft((x,c))
                
            while k < total_cost:
                value, c = q.pop()

                total_cost -= value - nums[right]
                right -= 1

                if c > 1:
                    q.append((value, c - 1))

            res += right - left + 1
        
        return res





       
        