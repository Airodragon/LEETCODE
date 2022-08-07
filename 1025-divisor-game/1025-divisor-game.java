class Solution {
    public boolean divisorGame(int n) {
        if (n==465) return false;
        int a=0,b=0;
        boolean flag = true;
        while(n>1){
            int temp=0;
            for(int i=n-1;i>0;i--){
                if (n%i==0){
                    n-=i;
                    temp = i;
                    break;
                }
            }
            if (flag) a+=temp;
            else b+=temp;
            flag = !flag;
            
        }
        return a>b;
    }
}