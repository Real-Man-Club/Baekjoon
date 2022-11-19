from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False for _ in range(f)]

def bfs():
    q = deque()
    q.append((s, 0))
    
    while q:
        now, count = q.popleft()
        
        if now == g:
            return count
        
        if 0 < now <= f and not visited[now]:
            visited[now] = True
            q.append((now + u, count + 1))
            q.append((now - d, count + 1))
    
    return 'use the stairs'

print(bfs())