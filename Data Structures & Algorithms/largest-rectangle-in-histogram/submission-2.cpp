class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int,int>> s;
        int m = 0;
        for (int i=0;i<heights.size();i++){
            int curr = i;
            while (!s.empty() && s.top().second >= heights[i]) {
                curr = s.top().first;

                int height = s.top().second;
                int width = i - curr;

                m = max(m, height * width);

                s.pop();
            }

            s.push({curr,heights[i]});
        }
        while (!s.empty()) {
            int index = s.top().first;
            int height = s.top().second;
            int width = heights.size() - index;

            m = max(m, height * width);

            s.pop();
        }
        return m;
    }
};
