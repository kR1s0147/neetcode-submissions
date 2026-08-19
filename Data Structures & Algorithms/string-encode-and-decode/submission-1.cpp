class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (string s : strs){
            res +=  to_string(s.size())+ "#" + s;
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int l = 0;
        while (l < s.size()) {
            string len_st;
            for(;l<s.size();l++){
                if (s[l] == '#'){
                    break;
                }
                len_st.push_back(s[l]);
            }
            int len = stoi(len_st);
            string t = s.substr(l+1, len);
            res.push_back(t);
            l = l + 1 + len;
        }
        return res;
    }
};
