class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> suffix(prices.size());
        int profit = 0;
        int t= 0;
        for(int i = prices.size()-1;i>=0;i--){
            suffix[i] = t;
            if (prices[i] > t){
                t = prices[i];
            }
        }

        for (int i =0;i<prices.size();i++){
            profit = max(profit , suffix[i]-prices[i]);
        }

        return profit;
    }
};
