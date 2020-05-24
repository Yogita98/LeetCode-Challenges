class Solution:
    def findComplement(self, num: int) -> int:
        if num==1:
            return 0
        
        bin_num="" 
        n=0
        
        while(num>=1):
            c=1-num%2
            num=num//2
            bin_num+=str(c)
        l=(list(map(int,bin_num)))
        print(len(l))
        
        for i in range(len(l)):
            n+=l[i]*pow(2,i)
            
        return n
        
 