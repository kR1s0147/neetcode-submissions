class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        unordered_map<char,char> m = {
            {')','('},
            {'}','{'},
            {']','['},
        };

      for (char c : s) {
            if (m.contains(c)) {
                if (st.empty() || m[c] != st.top()) {
                    return false;
                }

                st.pop();
            } else {
                st.push(c);
            }
        }

        return st.empty();
    }
};
