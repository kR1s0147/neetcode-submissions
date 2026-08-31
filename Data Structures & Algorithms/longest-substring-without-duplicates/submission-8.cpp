class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int j = 0;
        int res = 0;
        unordered_map<char,int> dup;

        while(j<s.size()){
            if (dup.contains(s[j])){
                i = max(i,dup[s[j]] + 1);
            }
            dup[s[j]] = j;
            res = max(res,(j-i + 1));
            j++;
        }
        return res;
    }
};
