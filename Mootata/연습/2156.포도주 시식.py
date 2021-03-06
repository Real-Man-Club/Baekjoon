n = int(input())
cups = []

for i in range(n):
    cups.append(int(input()))

if n == 1:
    print(cups[0])
    exit(0)

dp = [cups[0], cups[0] + cups[1]] + ([0] * n)

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + cups[i], dp[i - 3] + cups[i] + cups[i - 1])

print(dp[n - 1])