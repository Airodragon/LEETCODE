class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        int a[][] = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                a[i][j]=image[i][n-j-1];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
               if(a[i][j]==1) a[i][j]=0;
               else a[i][j]=1;
            }
        }
        
        return a;
    }
}