class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        num_communicating = 0
        column_to_num_row_singletons = dict()
        for i, row in enumerate(grid):
            num_ones = row.count(1)
            if num_ones > 1:
                num_communicating += num_ones
            elif num_ones == 1:
                column_ind = row.index(1)
                if column_ind in column_to_num_row_singletons:
                    column_to_num_row_singletons[column_ind] += 1
                else:
                    column_to_num_row_singletons[column_ind] = 1

        print('num_communicating', num_communicating, column_to_num_row_singletons)
        
        for j, num_singletons in column_to_num_row_singletons.items():
            num_ones = 0
            for i in range(m):
                num_ones += (grid[i][j] == 1)
                if num_ones > 1:
                    num_communicating += num_singletons
                    break

        return num_communicating