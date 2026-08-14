class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        for(int i=0;i<nums.size();i++){
            m[nums[i]] = i+1;
        }
        for(int i=0;i<nums.size();i++){
            int v = m[target-nums[i]];
            if (v > 0 && v-1 != i){
                return {i,v-1};
            } 
        }
        return {};
    }
};
