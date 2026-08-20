class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int,set<char>> rows;
        unordered_map<int,set<char>> cols;
        unordered_map<int,set<char>> grid;
        
        for(int row =0;row<9;row++){
            vector<char> curr_row = board[row];
            for(int col =0;col<9;col++){
                char curr = curr_row[col];
                if (curr == '.') {
                    continue;
                }
                // row check 
                set<char>& row_set = rows[row];
                if (row_set.count(curr)){
                    return false;
                } else {
                    row_set.insert(curr);
                }

                // colcheck
                set<char>& col_set = cols[col];
                if (col_set.count(curr)){
                    return false;
                } else {
                    col_set.insert(curr);
                }

                // grid check 
                int key = ((row / 3) * 3) + (col /3);
                set<char>& grid_set = grid[key];
                if (grid_set.count(curr)){
                    return false;
                } else {
                    grid_set.insert(curr);
                }
            }
        }

        return true;
    }
};
