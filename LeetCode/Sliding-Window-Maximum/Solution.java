1class Solution {
2    public int[] maxSlidingWindow(int[] nums, int k) {
3        int n=nums.length;
4        int[] result=new int[n-k+1];
5        Deque<Integer>d=new LinkedList<>();
6        for(int right=0;right<n;right++){
7            while(!d.isEmpty()&&d.peekFirst()<=right-k){
8                d.pollFirst();
9            }
10            while(!d.isEmpty() && nums[d.peekLast()]<nums[right]){
11                d.pollLast();
12            }
13            d.addLast(right);
14            if (right>=k-1){
15                result[right-k+1]=nums[d.peekFirst()];
16            }
17        }
18        return result;
19    }
20}