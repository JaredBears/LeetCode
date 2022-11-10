class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        origColor = image[sr][sc]
        def fill(r, c):
            if image[r][c] == origColor:
                image[r][c] = color
            else:
                return
            if r > 0:
                fill(r - 1, c)
            if r < len(image) - 1:
                fill(r + 1, c)
            if c > 0:
                fill(r, c - 1)
            if c < len(image[r]) - 1:
                fill(r, c + 1)
        fill(sr, sc)
        return image
