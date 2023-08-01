dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
answer = 0


def dfs(x, y, dist):
    global answer

    if (x, y) == (0, c - 1) and dist == k:
        answer += 1
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] == "T":
            continue

        board[nx][ny] = "T"
        dfs(nx, ny, dist + 1)
        board[nx][ny] = "."


board[r - 1][0] = "T"
dfs(r - 1, 0, 1)
print(answer)

# 1트 BFS로 했다가 방문처리 때문에 DFS로 변경
# 2트 방문처리를 visited로 했는데 그러면 모든 경우는 확인할 수 없음
# 3트 편의를 위해 (0, 0)에서 (r - 1, c - 1)로 가는 경로를 구했으나, (r - 1, c - 1)가 T일 수 있다는 것을 깜빡함
