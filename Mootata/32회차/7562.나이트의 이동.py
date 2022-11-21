from collections import deque

dx, dy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(x, y, tx, ty):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    
    while q:
        x, y, count = q.popleft()
        
        if tx == x and ty == y:
            return count
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= l or ny >= l or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

for t in range(int(input())):
    l = int(input())
    board = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    
    print(bfs(x, y, tx, ty))