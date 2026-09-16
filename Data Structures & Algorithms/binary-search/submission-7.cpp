class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binary(nums,target,0,nums.size()-1);
    }

    int binary(vector<int>& nums,int target,int l,int r){
         if (l > r) {
            return -1;
        }
        int mid = (l + r)/2;
        if (target > nums[mid]){
            return binary(nums,target,mid+1,r);
        } else if (target < nums[mid]){
            return binary(nums,target,l,mid-1);
        }
        return mid;
    }
};
