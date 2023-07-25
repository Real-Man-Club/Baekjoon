dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

board = [list(input().split()) for _ in range(5)]
answer = set()  # 중복 제거를 위한 set


def dfs(x, y, num):
    if len(num) == 6:  # 한칸씩 이동하면서 만든 숫자의 길이가 6이 되면 answer에 추가하고 멈춤
        answer.add(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:  # 범위 밖 벗어나면 패스
            continue

        dfs(nx, ny, num + board[nx][ny])


for i in range(5):  # 임의의 위치에서 시작해야하므로,
    for j in range(5):  # 모든 위치에서 시작
        dfs(i, j, board[i][j])

print(len(answer))
