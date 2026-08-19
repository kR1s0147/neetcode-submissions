class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_prod;
        vector<int> suffix_prod(nums.size());
        prefix_prod.push_back(1);
        for (int i =1;i<nums.size();i++){
            int prev = prefix_prod[i-1];
            prefix_prod.push_back(prev * nums[i-1]);
        }

        suffix_prod[nums.size() - 1] = 1;
        for (int i =nums.size() -2;i>=0;i--){
            int suff = suffix_prod[i+1];
            suffix_prod[i] = suff * nums[i+1];
        }

        for(int i=0;i<nums.size();i++){
            nums[i] = prefix_prod[i] * suffix_prod[i];
        }

        return nums;

    }
};
