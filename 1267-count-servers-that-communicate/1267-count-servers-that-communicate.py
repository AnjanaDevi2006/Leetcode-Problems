class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        c=0
        for i in grid:
            sm=sum(i)
            if sm==1:
                t=[l for l in range(len(i)) if i[l]==1] 
                cc=0
                for j in range(len(grid)):
                    if grid[j][t[0]]==1:
                        cc+=1
                if cc<2:
                    c-=1
            c+=sm
        return c