class Solution {
public:
    int trap(vector<int>& height) {
        int area =0 ;
        vector<int> prefix(height.size());
        vector<int> suffix(height.size());
        int t = 0;

        for(int i=0;i<height.size();i++){
            prefix[i] = t;
            if (height[i] > t){
                t = height[i];
            }
        }

        t = 0;
        for(int i=height.size()-1;i>=0;i--){
            suffix[i] = t;
            if (height[i] > t){
                t = height[i];
            }
        }

         for(int i=0;i<height.size();i++){
            int j = min(prefix[i],suffix[i]); 
            if (j > height[i]){
                area += j - height[i];
            }
        }
        return area;
    }
};
