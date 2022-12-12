from itertools import permutations

n = int(input())
number = list(map(int, input().split()))
answer = 0

for p in permutations(number):
    temp = 0
    for i in range(n - 1):
        temp += abs(p[i] - p[i + 1])
    answer = max(answer, temp)

print(answer)