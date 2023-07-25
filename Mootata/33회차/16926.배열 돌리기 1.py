from collections import deque

n, m, r = map(int, input().split())
a = [list(input().split()) for _ in range(n)]
q = deque()
answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(min(n, m) // 2):
    q = deque()
    q.extend(a[i][i : m - i])  # 상
    q.extend([j[m - i - 1] for j in a[i + 1 : n - i - 1]])  # 우
    q.extend(a[n - i - 1][i : m - i][::-1])  # 하
    q.extend([j[i] for j in a[i + 1 : n - i - 1]][::-1])  # 좌

    q.rotate(-r)

    for j in range(i, m - i):  # 위쪽
        answer[i][j] = q.popleft()
    for j in range(i + 1, n - i - 1):  # 오른쪽
        answer[j][m - i - 1] = q.popleft()
    for j in range(m - i - 1, i - 1, -1):  # 아래쪽
        answer[n - i - 1][j] = q.popleft()
    for j in range(n - i - 2, i, -1):  # 왼쪽
        answer[j][i] = q.popleft()

for a in answer:
    print(" ".join(a))

# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
