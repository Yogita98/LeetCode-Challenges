class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==1:
            return trust[0][1]
        if N==1:
            return 1

        dict_N={}
        for i in range(1,N+1):
            dict_N[i] = 0
        
        k=0
        for i in range(len(trust)):
            if dict_N[trust[i][1]]>0:
                dict_N[trust[i][1]] += 1
                if dict_N[trust[i][1]]==N-1:
                    k = trust[i][1]
                    break
            else:
                dict_N[trust[i][1]] = 1 
        for list in (trust):
            print(list[0])
            if list[0]==k or k==0:
                return -1
        return k