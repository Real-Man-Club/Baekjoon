n = int(input())
number = list(map(int, input().split()))

dp_B = [1 for _ in range(n)]
dp_S = [1 for _ in range(n)]

for i in range(1, n):
    if number[i] <= number[i - 1]:
        dp_B[i] = max(dp_B[i], dp_B[i - 1] + 1)
    if number[i] >= number[i-1]:
        dp_S[i] = max(dp_S[i], dp_S[i - 1] + 1)

print(max(max(dp_B), max(dp_S)))