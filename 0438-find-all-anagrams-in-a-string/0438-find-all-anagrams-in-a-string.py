from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(s) < len(p):
            return res
            
        pMap = defaultdict(int)
        sMap = defaultdict(int)
        
        for c in p:
            pMap[c] += 1
            
        left = 0
        count = len(p)
        
        for right in range(len(s)):
            ch = s[right]
            
            sMap[ch] += 1
            
            if ch in pMap and sMap[ch] <= pMap[ch]:
                count -= 1
                
            if right - left + 1 > len(p):
                leftChar = s[left]
                if leftChar in pMap and sMap[leftChar] <= pMap[leftChar]:
                    count += 1
                    
                sMap[leftChar] -= 1
                left += 1
                
            if count == 0:
                res.append(left)
                
        return res
