dp = [1 for _ in range(10001)]  # 모든 값은 1의 합으로 나타낼 수 있음

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for t in range(int(input())):
    n = int(input())
    print(dp[n])

# 1. 1
# 2. 1 + 1, 2
# 3. 1 + 1 + 1, 1 + 2, 3
# 4. 1 + 1 + 1 + 1, 1 + 1 + 2, 2 + 2, 1 + 3
# 5. 1 + 1 + 1 + 1 + 1, 1 + 1 + 1 + 2, 1 + 2 + 2, 3 + 2, 1 + 1 + 3
