1class Solution:
2    def uniformArray(self, a):
3        mn = float('inf')
4        oddCnt = 0
5        for x in a:
6            mn = min(mn, x)
7            if x % 2 == 1:
8                oddCnt += 1
9        # min Element is ODD(remaining even > min) or All Even!
10        return mn % 2 == 1 or oddCnt == 0