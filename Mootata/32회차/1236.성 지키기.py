n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

x, y = 0, 0

for i in castle:
    if 'X' not in i:
        x += 1

for i in range(m):
    if 'X' not in [castle[j][i] for j in range(n)]:
        y += 1

print(max(x, y))