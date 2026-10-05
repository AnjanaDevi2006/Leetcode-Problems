class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        len_s=len(s)
        len_p=len(p)
        if len_p>len_s:
            return res
        p_count=[0]*26
        s_count=[0]*26
        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        for ch in s[:len_p]:
            s_count[ord(ch)-ord('a')]+=1
        if p_count == s_count:
            res.append(0)
        for i in range(len_p,len_s):
            old_char=s[i-len_p]
            s_count[ord(old_char)-ord('a')]-=1

            new_char=s[i]
            s_count[ord(new_char)-ord('a')]+=1

            if s_count == p_count:
                res.append(i-len_p+1)
        return res