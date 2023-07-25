n = int(input())
xys = [tuple(map(int, input().split())) for _ in range(n)]

xys.sort(key = lambda x: (x[1], x[0]))

for i in xys:
    print(*i)