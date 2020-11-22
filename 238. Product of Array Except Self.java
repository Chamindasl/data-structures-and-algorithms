class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int right [] = new int [nums.length];
        int left [] = new int [nums.length];
        int result [] = new int [nums.length];
        int r = 1, l=1;
        for(int i = 0, j = size-1; i<size; i++, j--) {
            right[i] = r * nums[i];
            r = right[i];
            left[j] = l * nums[j];
            l = left[j];
        }
        result[0] = left[1];
        result[size-1] = right[size-2];
        for(int i = 1; i<size-1; i++) {
            result[i] = right[i-1] * left[i+1];
        }
        return result;
    }
   
}
