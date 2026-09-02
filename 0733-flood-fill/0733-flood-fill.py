class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        R, C = len(image), len(image[0])
        
        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and image[r][c] == orig:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
                
        dfs(sr, sc)
        return image