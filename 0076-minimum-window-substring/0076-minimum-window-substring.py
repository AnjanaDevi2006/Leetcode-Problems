class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
            
        sMap = {}
        
        left = 0
        count = len(t)
        minLen = float('inf')
        ans = ""
        
        for right in range(len(s)):
            ch = s[right]
            sMap[ch] = sMap.get(ch, 0) + 1
            
            if ch in tMap and sMap[ch] <= tMap[ch]:
                count -= 1
                
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    ans = s[left:right + 1]
                    
                leftChar = s[left]
                sMap[leftChar] -= 1
                
                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    count += 1
                    
                left += 1
                
        return ans
