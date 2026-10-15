class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        
        if n < 2:
            return ""
            
        res = ""
        
        for i in range(n):
            lower_set = set()
            upper_set = set()
            
            for j in range(i, n):
                if s[j].islower():
                    lower_set.add(s[j])
                else:
                    upper_set.add(s[j])
                    
                nice = True


                for c in lower_set:
                    if c.upper() not in upper_set:
                        nice = False
                        break

                for c in upper_set:
                    if c.lower() not in lower_set:
                        nice = False
                        break

                if nice and (j - i + 1) > len(res):
                    res = s[i:j + 1]

        return res
