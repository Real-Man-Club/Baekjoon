n, jm, hs = map(int, input().split())
answer = 0

while jm != hs:
    jm -= jm // 2
    hs -= hs // 2
    answer += 1

print(answer)