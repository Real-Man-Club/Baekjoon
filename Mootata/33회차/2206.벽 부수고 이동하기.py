from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 1


def bfs():
    q = deque([(0, 0, 1)])

    while q:
        x, y, b = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][b]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 1 and b == 1:  # 벽 부술 기회가 남아있으면 부숨
                visited[nx][ny][0] = visited[x][y][1] + 1
                q.append((nx, ny, 0))
            if maps[nx][ny] == 0 and not visited[nx][ny][b]:
                visited[nx][ny][b] = visited[x][y][b] + 1
                q.append((nx, ny, b))
    return -1


print(bfs())
