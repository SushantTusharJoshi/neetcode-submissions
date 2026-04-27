class Solution {
    public int climbStairs(int n) {

         int rob1 = 1;
         int rob2 = 1;

        for ( int i = 0; i< n - 1 ; i++){
            int temp = rob1;
            rob1 = rob1 + rob2;
            rob2 = temp;
        }


        return rob1;
        
    }
}
