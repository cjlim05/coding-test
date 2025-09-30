# from collections import deque

# def solution(maps):
#     answer = 0
#     rows, cols = len(maps), len(maps[0])
#     queue = deque([(0, 0, 1)])
    
#     direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
#     while queue: 
        
#         x, y, dist = queue.popleft()
        
#         if x == rows - 1 and y == cols - 1:
#             return dist
        
#         for dx, dy in direction:
#             nx, ny = x+dx, y+dy 
#             if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1:
#                 maps[nx][ny] = 0
#                 queue.append((nx, ny, dist + 1))
    
#     return -1

def solution(maps):
    h, w = len(maps), len(maps[0])
    visited = [[0]*w for _ in range(h)]  # 0 = 안 방문, 1 = 방문
    
    queue = [(0, 0, 1)]  # x, y, 현재 거리
    visited[0][0] = 1
    
    while queue:
        x, y, dist = queue.pop(0)  # FIFO
        
        # 도착하면 바로 반환
        if x == h-1 and y == w-1:
            return dist
        
        # 상하좌우 탐색
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist + 1))
    
    # 도착 불가
    return -1


    
    