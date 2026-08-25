class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i=0;i<nums.size();i++){
             if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i+1;
            int r = nums.size()-1;
            while (l<r){
                int target = -(nums[i]);
                if ((nums[l]+nums[r]) < target){
                    l++;
                    continue;
                }else if((nums[l]+nums[r]) > target){
                    r--;
                    continue;
                }
                res.push_back({nums[i],nums[l],nums[r]});
                l++;
                r--;
                 // Skip duplicate left values
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }

                    // Skip duplicate right values
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
            }
        }
        return res;
    }
};
