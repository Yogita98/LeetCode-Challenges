from collections import Counter
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        result = 0
        dict_seen = {0: -1}
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                count -= 1
            if n == 1:
                count += 1
                 
            if count in dict_seen:                       # You have been here before
                result = max(result, i-dict_seen[count]) # Get the furthest distance
            else:                     # You haven't been here before
                dict_seen[count] = i  # Mark it
                 
        return result