class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = {}
        for c in t:
            map[c] = map.get(c, 0) + 1
            
        left = 0
        count = len(t)
        minLen = float('inf')
        ans = ""
        
        for right in range(len(s)):
            ch = s[right]
            
            if ch in map:
                if map[ch] > 0:
                    count -= 1
                map[ch] -= 1
                
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    ans = s[left:right + 1]
                    
                leftChar = s[left]
                
                if leftChar in map:
                    map[leftChar] += 1
                    if map[leftChar] > 0:
                        count += 1
                        
                left += 1
                
        return ans
