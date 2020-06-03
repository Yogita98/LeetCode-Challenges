class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        
        a=0
        flag=0
        for i in range(len(coordinates)-2):
            a = coordinates[i][0] * (coordinates[i+1][1] - coordinates[i+2][1]) + coordinates[i+1][0] * (coordinates[i+2][1] - coordinates[i][1]) + coordinates[i+2][0] * (coordinates[i][1] - coordinates[i+1][1])
            if a!=0:
                flag=1
        if flag!=1:
            return True
        
        flag=0
        x,y=coordinates[1][0]-coordinates[0][0],coordinates[1][1]-coordinates[0][1]
        for i in range(1,len(coordinates)-1):
            if (coordinates[i+1][0]-coordinates[i][0]!=x or coordinates[i+1][1]-coordinates[i][1]!=y):
                flag=1
                
        if flag==1:
            return False
        else:
            return True