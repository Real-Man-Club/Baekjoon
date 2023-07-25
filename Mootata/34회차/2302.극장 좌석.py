n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0 for _ in range(n + 2)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1

if m > 0:
    pre = 0
    for j in range(m):  # vip 사이 그룹의 경우의 수
        answer *= dp[vip[j] - 1 - pre]
        pre = vip[j]
    answer *= dp[n - pre]
else:
    answer = dp[n]
print(answer)

# 1. 1 = 1
# 2. 1 2, 2 1 = 2
# 3. 1 2 3, 1 3 2, 2 1 3 = 3
# 4. 1 2 3 4, 1 3 2 4, 2 1 3 4, 1 2 4 3, 2 1 3 4 = 5
# 5. 1 2 3 4 5, 1 3 2 4 5, 2 1 3 4 5, 1 2 4 3 5, 2 1 3 4 5, 1 2 3 5 4, 1 3 2 5 4, 2 1 3 5 4 = 8

# dp[n] = dp[n - 1] + dp[n - 2]
