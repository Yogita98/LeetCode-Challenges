from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_string=Counter(s)
        j=-1
        
        for k,v in dict_string.items():
            j+=1
            if(v==1):
                return s.index(k)
            
        return -1