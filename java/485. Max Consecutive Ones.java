class Solution {
    public int findMaxConsecutiveOnes(int[] a) {
        int max = 0;
        int currMax = 0;
        for (int i =0; i<a.length;i++) {
            if (a[i]==1) {
                currMax++;
            } else {
                max = Math.max(max, currMax);
                currMax = 0;
            }
        }
        return Math.max(max, currMax);
    }
}
