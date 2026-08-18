1class Solution:
2    def findSubstring(self, s: str, words: List[str]) -> List[int]:
3        word_freq = defaultdict(int)
4        for word in words:
5            word_freq[word] += 1
6
7        word_len = len(words[0])
8        # words of the same length
9        window = len(words) * word_len
10        ans = []
11
12        for i in range(len(s) - window + 1):
13            substr_freq = defaultdict(int)
14            j = i
15
16            while j < i + window:
17                current = s[j : j + word_len]
18                if current not in word_freq:
19                    break
20
21                substr_freq[current] += 1
22                if substr_freq[current] > word_freq[current]:
23                    break
24
25                j += word_len
26            
27            if j == i + window:
28                ans.append(i)
29
30        return ans
31        