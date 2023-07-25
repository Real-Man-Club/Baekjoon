from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

m, n, k = map(int, input().split())
paper = [[0 for _ in range(m)] for _ in range(n)]
answer = []


for i in range(k):
    lx, ly, rx, ry = map(int, input().split())

    for j in range(lx, rx):
        for l in range(ly, ry):
            paper[j][l] = 1


def bfs(x, y):
    q = deque([(x, y)])
    paper[x][y] = 1
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or paper[nx][ny]:
                continue

            count += 1
            paper[nx][ny] = 1
            q.append((nx, ny))

    return count


for i in range(n):
    for j in range(m):
        if not paper[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
print(*sorted(answer))
