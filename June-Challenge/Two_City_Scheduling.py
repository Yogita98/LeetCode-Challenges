class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost=0  # To keep the minimum cost
        
        sorted_cost=sorted(costs,key= lambda x: x[0]-x[1]) # Sort the array on the basis of difference between                                                            # the cost of two cities
        # print(sorted_cost)
        for i in range(len(costs)):
            if i<len(costs)/2:         # This ensures that exactly N people arrive in each city
                min_cost+=sorted_cost[i][0]
            else:
                min_cost+=sorted_cost[i][1]
            
        return min_cost
        
        
# Reference: https://www.youtube.com/watch?v=2U5KkOy9pRE