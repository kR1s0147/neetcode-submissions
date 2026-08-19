class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int ,int> freq;
        for (int i:nums){
            freq[i]++;
        }

        vector<pair<int,int>> m;
       
        for (auto [key,value] : freq) {
            m.push_back({value,key});
        }

    sort(m.begin(),m.end(), greater<pair<int, int>>());

    vector<int> res;

    for (int i = 0;i<k;i++) {
       pair<int,int> t = m[i];
       res.push_back(t.second);
    }
    return res;
        
    }
};
