class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s

        nxt = "".join(str(sum(int(c) for c in s[i:i + k]))
                      for i in range(0, len(s), k))

        return self.digitSum(nxt, k)