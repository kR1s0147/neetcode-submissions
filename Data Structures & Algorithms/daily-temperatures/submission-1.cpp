class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> s;
        vector<int> res(temperatures.size());
        for (int i=0;i<temperatures.size();i++){
            while ((s.size()>0) && (temperatures[i]>temperatures[s.top()])){
                int j = s.top();
                s.pop();
                res[j]=(i-j);
            }
            s.push(i);
        }
        return res;
    }
};
