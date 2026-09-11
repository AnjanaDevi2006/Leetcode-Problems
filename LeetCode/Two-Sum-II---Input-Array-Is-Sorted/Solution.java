1class Solution {
2    public int[] twoSum(int[] numbers, int target) {
3        
4        int n=numbers.length;
5        int left=0;
6        int right=n-1;
7        while(left<right){
8            int sum=numbers[left]+numbers[right];
9            if(sum==target){
10                return new int[]{left+1,right+1};
11            }
12            else if(sum>target){
13                right--;
14            }
15            else{
16                left++;
17            }
18        }
19        return new int[]{-1,-1};
20    }
21}