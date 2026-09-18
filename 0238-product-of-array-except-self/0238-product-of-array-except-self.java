class Solution {
    public int[] productExceptSelf(int[] nums) {
       int n=nums.length;
       int[] res=new int[n];
       res[0]=1;
       for(int i=1;i<n;i++){
        res[i]=res[i-1]*nums[i-1];
       } 
       int rightprod=1;
       for(int r=n-1;r>=0;r--){
        res[r]=res[r]*rightprod;
        rightprod*=nums[r];
       }
       return res;
    }
}