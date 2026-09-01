class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char ,int> count1;
        unordered_map<char ,int> count2;
        for (char c : s1){
            count1[c]++;
        }

        int i = 0;
        for(int r = 0;r<s2.size();r++){
            count2[s2[r]]++;
            while((r-i+1)>s1.size()){
                count2[s2[i]]--;
                if(count2[s2[i]]==0){
                    count2.erase(s2[i]);
                }
                i++;
            }
            if (count1 == count2){
                return true;
            }
        }
        return false;

    }
};
