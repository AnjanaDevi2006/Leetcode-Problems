1class Solution {
2public:
3    bool isPalindrome(string s) {
4        int left=0;
5        int right=s.length()-1;
6        while (left<right){
7            if (!isalnum(s[left])){
8                left++;
9            }
10            else if(!isalnum(s[right])){
11                right--;
12            }
13            else{
14                if(tolower(s[left])!=tolower(s[right])){
15                    return false;
16                }
17                left++;
18                right--;
19            }
20        }
21        return true;
22    }
23};