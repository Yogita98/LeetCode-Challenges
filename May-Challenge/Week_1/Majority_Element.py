from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_num=Counter(nums)
        for k,v in dict_num.items():
            if v>(len(nums)/2):
                return k
        