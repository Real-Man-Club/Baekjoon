n = int(input())
numbers = list(map(int, input().split()))
sn = sorted(numbers)
answer = []

for i in range(n):
    idx = sn.index(numbers[i])
    answer.append(idx)
    sn[idx] = 1001

print(*answer)