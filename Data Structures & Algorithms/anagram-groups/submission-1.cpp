class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<int,vector<int>> freq;
        int len = strs.size();
        for (int i=0;i<len;i++){
            vector<int> in_freq(26);
            for (char c : strs[i]){
                in_freq[c - 'a']++;
            }
            freq[i] = in_freq;
        }

        map<vector<int>,vector<string>> out_freq;
        for(int i =0;i<len;i++){
            vector<int> in_map = freq[i];
            out_freq[in_map].push_back(strs[i]);
        }

        vector<vector<string>> res;
        for (auto& [key,str] : out_freq) {
            res.push_back(str);
        }
        return res;
    }
};
