# 733. Flood Fill

# TC : O(N), where N is the number of pixels in the image.
# SC : O(N) in worst case, but typically better than the recursive approach as it eliminates recursion overhead.
# Did this code successfully run on Leetcode : Yes

# Approach :
# Iterative Approach: Replaced recursion with an iterative stack-based approach to eliminate the function call overhead and reduce the risk of stack overflow for large images.
# Direction Array: Used a directions array to make the code more concise and clearer when checking adjacent pixels.
# Early Color Check: We check if a pixel has the original color before processing it, which avoids duplicate stack entries and unnecessary checks.
# Process During Pop: We only process a pixel when we pop it from the stack, ensuring each pixel is processed exactly once.
# Push Only Valid Neighbors: We only add neighbors to the stack if they are within bounds and have the original color, saving space and avoiding redundant checks later.

from typing import List, Optional

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Early return if the starting pixel is already the target color
        if image[sr][sc] == color:
            return image
        
        # Get dimensions and original color
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # Define directions for adjacent pixels (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Use stack-based iterative approach instead of recursion
        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            
            # Process current pixel
            if image[r][c] == original_color:
                image[r][c] = color
                
                # Add valid adjacent pixels to the stack
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        image[nr][nc] == original_color):
                        stack.append((nr, nc))
                        
        return image