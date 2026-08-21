class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(),nums.end());
        int l = 0;
        for(int n : s){
            if (!s.contains(n-1)) {
                int curr = n;
                int len = 0;
                while (s.contains(curr)){
                     len++;
                     curr++;
                }
                l = max(len,l);
            }
        }

        return l;
    }
};
