class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        def helper( person_id, color ):
            color_table[person_id] = color
            for the_other in dislike_table[ person_id ]:
                if color_table[the_other] == color:
                    return False

                if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                    return False
                    
            return True
        
        if N == 1 or not dislikes:
            return True
        
        dislike_table = collections.defaultdict( list )
        color_table = [ NOT_COLORED for _ in range(N+1) ]
        
        for p1, p2 in dislikes:
            
            # P1 and P2 dislike each other
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        for person_id in range(1, N+1):
            
            if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                return False 
        
        return True