from collections import deque

dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

n = int(input())
sx, sy, ex, ey = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((sx, sy, 0))
    visited[sx][sy] = True
    
    while q:
        x, y, count = q.popleft()
        
        if x == ex and y == ey:
            return count
        
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            
            q.append((nx, ny, count + 1))
            visited[nx][ny] = True
            
    return -1


print(bfs())