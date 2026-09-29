    if(i==grid.size()-1 && j==grid[0].size()-1 && lefts==1 && grid[i][j]==')') {
        return true;
    }
    if(i==grid.size() || j == grid[0].size()) return false;
    
    if(dp[i][j][lefts]!=-1) return dp[i][j][lefts];
    
    if (grid[i][j] == '(')
        lefts++;
    else if(grid[i][j]==')' && lefts>0)
        lefts--;
    else 
        return dp[i][j][lefts]=false;
    
    bool found = false;
    if(i+1<grid.size())
        found |= recurse( grid, i+1, j, lefts);
    if(j+1<grid[0].size())
        found |= recurse( grid, i, j+1, lefts);
    
    return dp[i][j][lefts]=found;
        
}
bool hasValidPath(vector<vector<char>>& grid) {
    memset(dp, -1, sizeof(dp));
    return recurse(grid, 0, 0, 0);     
}