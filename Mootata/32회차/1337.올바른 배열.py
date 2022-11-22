n = int(input())
arr = sorted([int(input()) for _ in range(n)])
answer = 5


for i in arr:
    count = 0
    for j in range(i + 1, i + 5):
        if j not in arr:
            count += 1
    
    answer = min(answer, count)

print(answer)