class Solution:
    def maxDepthAfterSplit(self, seq: str):
        return [(i + (c == '(')) % 2 for i, c in enumerate(seq)]