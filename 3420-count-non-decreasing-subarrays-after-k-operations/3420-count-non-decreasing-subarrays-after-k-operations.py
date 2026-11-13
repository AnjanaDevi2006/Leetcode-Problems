
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = n - 1
        ans = cost = 0
        dq = deque()

        for i in range(n - 1, -1, -1):
            cnt = 1

            while dq and dq[-1][0] < nums[i]:
                v, c = dq.pop()
                cnt += c
                cost += (nums[i] - v) * c

            dq.append((nums[i], cnt))

            while cost > k:
                v, c = dq.popleft()
                cost -= v - nums[j]
                j -= 1

                if c > 1:
                    dq.appendleft((v, c - 1))

            ans += j - i + 1

        return ans