class Solution {
    public void rotate(int[][] m) {
        int size = m.length -1;
        for (int level=0; level<m.length/2;level++) {
            for(int i = level; i<size-level; i++) {
                int temp = m[level][i];
                m[level][i] = m[size-i][level];
                m[size-i][level] = m[size-level][size-i];
                m[size-level][size-i] = m[i][size-level]; 
                m[i][size-level] = temp;
            }
        }
            
    }
}
