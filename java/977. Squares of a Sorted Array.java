class Solution {
    public int[] sortedSquares(int[] a) {
        int left = 0, right = a.length - 1;
        int idx = a.length - 1;
        int resut [] = new int [a.length];
        while(left<=right) {
            int leftSqr = a[left] * a[left]; 
            int rightSqr = a[right] * a[right]; 
            if (leftSqr>rightSqr) {
                resut[idx--] = leftSqr;
                left++;
            } else {
                resut[idx--] = rightSqr;
                right--;
            }
        }
        return resut;
    }
}
