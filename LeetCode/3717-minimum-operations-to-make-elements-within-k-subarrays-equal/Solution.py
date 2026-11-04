class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        # Initial left/right half of sorted window
        half = x // 2
        LR = sorted(nums[:x])
        L = SortedList(LR[:half])
        R = SortedList(LR[half:])
        sumL, sumR = sum(L), sum(R)

        # Cost of initial window
        median = R[0]
        cost = (half * median - sumL) + (sumR - (x-half) * median)
        costs = [cost]

        # Slide the window
        for remove, add in zip(nums, nums[x:]):

            # Add/remove the numbers entering/leaving the window
            if add < R[0]:
                L.add(add)
                sumL += add
            else:
                R.add(add)
                sumR += add
            if remove < R[0]:
                L.remove(remove)
                sumL -= remove
            else:
                R.remove(remove)
                sumR -= remove

            # Restore the correct half-window sizes
            if len(L) < half:
                L.add(move := R.pop(0))
                sumL += move
                sumR -= move
            elif len(L) > half:
                R.add(move := L.pop(-1))
                sumL -= move
                sumR += move

            # Collect the new cost
            median = R[0]
            cost = (half * median - sumL) + (sumR - (x-half) * median)
            costs.append(cost)

        # DP
        minCost = repeat(0)
        for _ in range(k):
            minCost = list(accumulate(map(operator.add, minCost, costs), min))
            del costs[:x]
        return minCost[-1]