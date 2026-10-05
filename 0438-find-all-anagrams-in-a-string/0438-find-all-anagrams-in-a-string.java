class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        
        int n = s.length();
        int k = p.length();
        
        int[] pCount = new int[26];
        for (char c : p.toCharArray()) {
            pCount[c - 'a']++; // 1000
        }
        
        for (int i = 0; i <= n - k; i++) { // 9000
            int[] sCount = new int[26];
            
            for (int j = i; j <= i + k - 1; j++) { // 1000
                sCount[s.charAt(j) - 'a']++;
            }
            
            if (Arrays.equals(pCount, sCount)) {
                res.add(i);
            }
        }
        
        return res;
    }
}
