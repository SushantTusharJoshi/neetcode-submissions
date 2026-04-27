class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> count = new HashMap();

        for (int i = 0; i< nums.length ; i++){
            int j = target - nums[i];


            if (count.containsKey(j)){
                return new int[]{
                    count.get(j),
                    i
                     };
            
            
        }

        count.put(nums[i],i);
        }

        return new int[]{
            -1,-1
        };
        

    }
}
