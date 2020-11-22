class Solution {
    public boolean validPalindrome(String s) {
        
        int p1 = 0, p2 = s.length() - 1;
        while(p1<=p2) {
            if(s.charAt(p1)==s.charAt(p2)) {
                p1++; 
                p2--;
            } else {
                if(isPalindrome(s, p1+1, p2) || isPalindrome(s, p1, p2 -1)) return true;
                return false;
            }
        }
        return true;
    }
    
    private boolean isPalindrome(String s, int start, int end) {
        while(start<=end) {
            if (s.charAt(start++)!=s.charAt(end--)) return false;
        }
        return true;
    }
}
