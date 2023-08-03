n, m = map(int, input().split())
board = [[True for _ in range(m)] for _ in range(n)]
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
answer = 0


def k_check(x, y):
    for i, j in [
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
    ]:
        nx, ny = x + i, y + j

        if (
            nx < 0
            or ny < 0
            or nx >= n
            or ny >= m
            or board[nx][ny] == "P"
            or board[nx][ny] == "K"
        ):
            continue

        board[nx][ny] = False


def q_check(x, y):
    board[x][y] = False

    for i in range(1, max(n, m)):  # 오른쪽 아래 대각선
        nx, ny = x + i, y + i
        if (
            nx < 0
            or ny < 0
            or nx >= n
            or ny >= m
            or board[nx][ny] == "P"
            or board[nx][ny] == "K"
        ):
            break

        board[nx][ny] = False

    for i in range(1, max(n, m)):  # 왼쪽 아래 대각선
        nx, ny = x + i, y - i
        if (
            nx < 0
            or ny < 0
            or nx >= n
            or ny >= m
            or board[nx][ny] == "P"
            or board[nx][ny] == "K"
        ):
            break

        board[nx][ny] = False

    for i in range(1, max(n, m)):  # 오른쪽 위 대각선
        nx, ny = x - i, y + i
        if (
            nx < 0
            or ny < 0
            or nx >= n
            or ny >= m
            or board[nx][ny] == "P"
            or board[nx][ny] == "K"
        ):
            break

        board[nx][ny] = False

    for i in range(1, max(n, m)):  # 왼쪽 위 대각선
        nx, ny = x - i, y - i
        if (
            nx < 0
            or ny < 0
            or nx >= n
            or ny >= m
            or board[nx][ny] == "P"
            or board[nx][ny] == "K"
        ):
            break

        board[nx][ny] = False

    for i in range(1, n):  # 위
        nx = x - i
        if nx < 0 or board[nx][y] == "P" or board[nx][y] == "K":
            break

        board[nx][y] = False

    for i in range(1, n):  # 아래
        nx = x + i
        if nx >= n or board[nx][y] == "P" or board[nx][y] == "K":
            break

        board[nx][y] = False

    for i in range(1, max(n, m)):  # 왼쪽
        ny = y - i
        if ny < 0 or board[x][ny] == "P" or board[x][ny] == "K":
            break

        board[x][ny] = False

    for i in range(1, max(n, m)):  # 오른쪽
        ny = y + i
        if ny >= m or board[x][ny] == "P" or board[x][ny] == "K":
            break

        board[x][ny] = False


for i in range(1, p[0] + 1):
    board[p[(i * 2) - 1] - 1][p[(i * 2)] - 1] = "P"

for i in range(1, k[0] + 1):
    x, y = k[(i * 2) - 1] - 1, k[(i * 2)] - 1
    board[x][y] = "K"
    k_check(x, y)

for i in range(1, q[0] + 1):
    x, y = q[(i * 2) - 1] - 1, q[(i * 2)] - 1
    board[x][y] = "Q"
    q_check(x, y)

for i in board:
    answer += i.count(True)

print(answer)
