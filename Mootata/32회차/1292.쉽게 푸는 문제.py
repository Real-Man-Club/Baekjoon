a, b = map(int, input().split())
answer = [0]

for i in range(b + 1):
    for j in range(i):
        answer.append(i)

print(sum(answer[a:b + 1]))