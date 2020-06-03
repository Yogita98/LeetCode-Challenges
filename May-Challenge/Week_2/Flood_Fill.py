class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
    
        num_rows, num_cols = len(image), len(image[0])
        og_color = image[sr][sc]
        
        if og_color == newColor:
            return image
        
        def change_pixels(sr1, sc1):
            if not (0 <= sr1 < num_rows and 0 <= sc1 < num_cols and image[sr1][sc1] == og_color):
                return None
            image[sr1][sc1] = newColor
            change_pixels(sr1 - 1, sc1)
            change_pixels(sr1 + 1, sc1)
            change_pixels(sr1, sc1 - 1)
            change_pixels(sr1, sc1 + 1)
                
        change_pixels(sr, sc)
        return image
        