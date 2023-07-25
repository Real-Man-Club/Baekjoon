n, t = map(int, input().split())
carrots = [list(map(int, input().split())) for _ in range(n)]
carrots.sort(key = lambda x: x[1])
answer = 0
day = t - n

for w, p in carrots:
    answer += w + (p * day)
    day += 1

print(answer)