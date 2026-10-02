1class Solution {
2    public boolean isPalindrome(String s) {
3        int left=0;
4        int right=s.length()-1;
5        while (left<right){
6            char l=s.charAt(left);
7            char r=s.charAt(right);
8            if (!isAlphaNum(l)){
9                left++;
10            }
11            else if(!isAlphaNum(r)){
12                right--;
13            }
14            else{
15                if(Character.toLowerCase(l)!=Character.toLowerCase(r)){
16                    return false;
17                }
18                left++;
19                right--;
20            }
21        }
22        return true;
23    }
24    private boolean isAlphaNum(char c){
25        return (c>='a'&&c<='z')||
26                (c>='A'&&c<='Z')||
27                (c>='0'&&c<='9');
28    }
29}
30
31
32