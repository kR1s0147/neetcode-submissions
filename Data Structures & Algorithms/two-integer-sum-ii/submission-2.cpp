class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        while (i < j) {
            int s = numbers[i] + numbers[j];
            if (s<target){
                i++;
                continue;
            }

            if (s>target){
                j--;
                continue;
            }
            return {i+1,j+1};
        }
        return {-1,-1};
    }
};
