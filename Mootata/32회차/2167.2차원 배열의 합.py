n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    answer = 0
    i, j, x, y = map(int, input().split())
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            answer += arr[a][b]
    print(answer)