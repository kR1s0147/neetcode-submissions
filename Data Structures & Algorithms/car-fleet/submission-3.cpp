class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        
        vector<pair<int,int>> t;
        for (int i =0 ;i<position.size();i++){
            t.push_back({position[i],speed[i]});
        }
        sort(t.begin(),t.end(),greater<pair<int,int>>());
        int res = 0;
        double max_time = 0;
        for (auto p:t){
            double time = (double)(target - p.first) / p.second ;
            if (time > max_time) {
                res+=1;
                max_time = time;
            }
        }
        return res;
    }
};
