from collections import deque

def solution(maps):
    answer = 0
    rows, cols = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while queue: 
        
        x, y, dist = queue.popleft()
        
        if x == rows - 1 and y == cols - 1:
            return dist
        
        for dx, dy in direction:
            nx, ny = x+dx, y+dy 
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, dist + 1))
    
    return -1
    