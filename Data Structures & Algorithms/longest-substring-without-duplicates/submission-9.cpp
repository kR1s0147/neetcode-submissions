class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int j = 0;
        int res = 0;
        unordered_set<char> dup;

        while(j<s.size()){
            while (dup.contains(s[j])) {
                dup.erase(s[i]);
                i++;
            }
            dup.insert(s[j]);
            res = max(res,(j - i + 1));
            j++;
        }
        return res;
    }
};
