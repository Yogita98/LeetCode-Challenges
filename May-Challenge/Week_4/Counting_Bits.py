class Solution:
    def countBits(self, num: int) -> List[int]:
        L=[]
        for i in range(num+1):
            L.append(bin(i)[2:].count('1'))
        return L