answer = float('inf')
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x <= y:
        answer = min(answer, y)
print(-1 if answer == float('inf') else answer)
