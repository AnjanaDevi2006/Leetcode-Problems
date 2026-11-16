class Solution:
    def digitSum(self, s: str, k: int) -> str:
        cur = [int(c) for c in s]

        while len(cur) > k:
            nxt = []
            for i in range(0, len(cur), k):
                total = sum(cur[i:i + k])
                nxt.extend(int(d) for d in str(total))
            cur = nxt

        return "".join(map(str, cur))