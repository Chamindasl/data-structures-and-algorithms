// https://leetcode.com/problems/search-in-rotated-sorted-array/solution/

class Solution {
    public int getRotateIdx(int nums []) {
        int size = nums.length - 1;
        if (nums[0]<nums[size] || size <= 0) return 0;
        int left = 0, mid, right = size;
        mid = right /2 ;
        while(!(nums[mid]>nums[mid+1])) {
            mid = left + (right - left) /2 ;
            if(nums[left]<nums[mid]) left = mid;
            else right = mid;
        }
        return mid + 1;
    }

    public int binarySearch(int nums[], int target, int left, int right) {
        while(left<=right) {
            int mid = left + (right-left)/2;
            if(nums[mid] == target) return mid;
            if(nums[mid]<target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

  public int search(int[] nums, int target) {
      int left = 0, right = nums.length - 1;
      int rotateIdx = getRotateIdx(nums);
      int targetIdx = binarySearch(nums, target, left, rotateIdx - 1);
      if (targetIdx == -1)
          targetIdx = binarySearch(nums, target, rotateIdx, right);
      return targetIdx;
  }

}
