class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i : nums) {
            if(!set.add(i)) {
                set.remove(i);
            }
        }
        for(int i : set) {
            return i;
        }
        return Integer.MAX_VALUE;
    }
}
