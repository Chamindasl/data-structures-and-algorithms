class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> items = new HashSet(nums.length);
        for(int num : nums) {
            if (!items.add(num)) return true;
        }
        return false;
    }
}
