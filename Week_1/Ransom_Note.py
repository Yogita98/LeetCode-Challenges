class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        flag=0
        for i in list(ransomNote):
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        for i in list(magazine):
            if i in d2.keys():
                d2[i]+=1
            else:
                d2[i]=1
        for key in d1.keys():
            if key in d2.keys():
                if d1[key]>d2[key]:
                    flag=1
            else:
                flag=1
        
        if flag==1:
            return False
        else:
            return True