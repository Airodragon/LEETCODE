class Solution {
    public static char[] ch = {'a','b','c',
             'd','e','f',
             'g','h','i',
             'j','k','l',
             'm','n','o',
             'p','q','r',
             's','t','u',
             'v','w',
             'x','y','z'};
    public boolean checkIfPangram(String s) {
        for(int i=0;i<ch.length;i++){
                if (s.indexOf(ch[i]) == -1) return false;
        }
        return true;
    }
}