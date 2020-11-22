class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int right [] = new int [nums.length];
        int left [] = new int [nums.length];
        int result [] = new int [nums.length];
        right[0] = 1;
        left[size-1] = 1;
        for(int i = 1; i<size; i++) {
            right[i] = right[i-1] * nums[i-1];
        }
        for(int i = size - 2; i>=0; i--) {
            left[i] = left[i+1] * nums[i+1];
        }
        for(int i = 0; i<size; i++) {
            result[i] = right[i] * left[i];
        }
        return result;
    }
   
}
