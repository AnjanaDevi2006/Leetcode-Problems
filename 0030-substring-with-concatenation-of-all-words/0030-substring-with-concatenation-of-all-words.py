
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        n, k = len(s), len(words[0])
        total = len(words)
        expected = Counter(words)

        for offset in range(k):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, n - k + 1, k):
                word = s[right:right + k]

                if word not in expected:
                    seen.clear()
                    count = 0
                    left = right + k
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > expected[word]:
                    seen[s[left:left + k]] -= 1
                    left += k
                    count -= 1

                if count == total:
                    res.append(left)

        return res
