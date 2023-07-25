n = int(input())
score = list(map(int, input().split()))
m = max(score)
answer = 0

for s in score:
    answer += (s / m) * 100

print(answer / len(score))