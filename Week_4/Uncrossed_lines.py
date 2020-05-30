class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
#         A = [ -1 ] + A
#         B = [ -1 ] + B
        
        len_A,len_B=len(A),len(B)
        # len_B=len(B)
        
        if len_A == 0 or len_B == 0:
            return 0
        
        dp = [ [ 0 for _ in range(len_B+1) ] for _ in range(len_A+1) ]
        
        for i in range(len_A):
            for j in range(len_B):
                if A[i]==B[j]:
                    dp[i+1][j+1]=1+dp[i][j]  
                    # dp[i+1][j+1]: Since the first row and first column has been zero-padded
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j]) # Taking the max of (top,left)
        
        return dp[-1][-1]