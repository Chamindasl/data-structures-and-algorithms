class Solution {
    public int removeDuplicates(int[] n) {
        if (n.length == 0) return 0;
        int newPointer = 1;
        int count = 1;
        for(int i=1;i<n.length;i++) {
            if(n[newPointer - 1] != n[i]){
                n[newPointer++] =n[i];
                count++;
            }
        }
        return count;
    }
}
