class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_ending_here=A[0]
        max_so_far=A[0]
        current_max=0
        current_min=0
        min_ending_here=A[0]
        min_so_far=A[0]
        sum_arr=A[0]
        
        for i in range(1,len(A)):
            current_max=max(A[i],current_max+A[i])
            max_so_far=max(current_max,max_so_far)
            current_min=min(A[i],current_min+A[i])
            min_so_far=min(current_min,min_so_far)
            sum_arr+=A[i]
        print(sum_arr)
        print(max_so_far)
        print(min_so_far)
            
        if sum_arr==min_so_far:
            return max_so_far
        
        return max(max_so_far,sum_arr-min_so_far,sum_arr)
        