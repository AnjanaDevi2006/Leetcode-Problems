import java.util.*;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();

        int wordLen = words[0].length();
        int total = wordLen * words.length;

        String[] sortedWords = words.clone();
        Arrays.sort(sortedWords);

        for (int i = 0; i <= s.length() - total; i++) {
            String sub = s.substring(i, i + total);
            String[] arr = new String[words.length];

            for (int j = 0; j < words.length; j++) {
                arr[j] = sub.substring(j * wordLen, (j + 1) * wordLen);
            }

            Arrays.sort(arr);

            if (Arrays.equals(arr, sortedWords)) {
                res.add(i);
            }
        }

        return res;
    }
}
