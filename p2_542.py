# 542. 01 Matrix

# TC : O(rows × cols), as each cell is processed at most once.
# SC : O(rows × cols) for the result matrix and the queue.
# Did this code successfully run on Leetcode : Yes

# Approach :
# BFS naturally finds the shortest paths when all edges have the same weight (in this case, each step has a distance of 1).
# Start by placing all cells with value 0 in the queue with distance 0.
# For each cell in the queue, we check its four adjacent neighbors:
    # If we find a shorter path to a neighbor, we update its distance and add it to the queue.
# Since we process cells in order of increasing distance from 0 cells, the first time we reach a cell is guaranteed to be via the shortest path.

from typing import List, Optional


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        # Initialize result matrix with maximum possible values
        result = [[float('inf')] * cols for _ in range(rows)]
        
        # Queue for BFS (using collections.deque would be more efficient)
        queue = []
        
        # Add all 0 cells as starting points for the BFS
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))
        
        # Directions for adjacent cells: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Process cells in breadth-first order
        while queue:
            r, c = queue.pop(0)  # This is inefficient for large queues, ideally use collections.deque
            
            # Check all adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If the adjacent cell is within bounds and we can improve its distance
                if (0 <= nr < rows and 0 <= nc < cols and 
                    result[nr][nc] > result[r][c] + 1):
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr, nc))
        
        return result
        