class Solution {
    public boolean isMonotonic(int[] A) {
        if (A.length == 1) return true;
        int inc = 0;
        for(int i=0; i<A.length - 1; i++) {
            if(inc==1) {
                if (A[i]>A[i+1]) return false;
            } else if(inc==-1) {
                if (A[i]<A[i+1]) return false;
            } else {
                if (A[i]<A[i+1]) inc = +1;
                else if (A[i]>A[i+1]) inc = -1;
            }
        }
        return true;
    }
}
