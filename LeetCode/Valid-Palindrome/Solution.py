1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l=0
4        r=len(s)-1
5        while l<r:
6            if not s[l].isalnum():
7                l+=1
8            elif not s[r].isalnum():
9                r-=1
10            else:
11                if s[l].lower()!=s[r].lower():
12                    return False
13                l+=1
14                r-=1
15        return True
16        