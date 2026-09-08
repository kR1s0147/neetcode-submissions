class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
       for (string t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {

                int p2 = s.top();
                s.pop();

                int p1 = s.top();
                s.pop();

                if (t == "+") {
                    s.push(p1 + p2);
                } 
                else if (t == "-") {
                    s.push(p1 - p2);
                } 
                else if (t == "*") {
                    s.push(p1 * p2);
                } 
                else {
                    s.push(p1 / p2);
                }

            } else {
                s.push(stoi(t));
            }
        }

        return s.top();
                 

    }
};
