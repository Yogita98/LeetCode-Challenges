class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n_rows=(len(matrix))
        n_cols=(len(matrix[0]))
        count=0
        
        
        if not n_rows:
            return 0
        
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j]:
                    if i>0 and j>0:
                    # print(matrix[i][j])
                        matrix[i][j]+=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    # print(matrix[i][j])
                count+=matrix[i][j]
                # print(count)
        return count