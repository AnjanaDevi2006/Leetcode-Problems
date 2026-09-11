1class Solution {
2    public int maxArea(int[] height) {
3        int n=height.length;
4        int left=0,right=n-1;
5        int maxArea=0;
6        while(left<=right){
7            int h=Math.min(height[left],height[right]);
8            int w=right-left;
9            int area=h*w;
10            maxArea=Math.max(maxArea,area);
11            if(height[left]<=height[right]){
12                left++;
13            }
14            else{
15                right--;
16            }
17            
18        }
19        return maxArea;
20    }
21}