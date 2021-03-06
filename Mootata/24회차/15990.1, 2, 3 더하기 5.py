t = int(input())

dp = [[0 for _ in range(3)] for _ in range(100001)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] += dp[i - j - 1][k]
                dp[i][j] %= 1000000009

for i in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)

# 예를 들어 i가 10일 때
# dp[9]의 2, 3으로 끝난 경우의 수에 1을 더하면 10이 되기 떄문에 두 경우의 수를 더한 값을 dp[10][0]에 넣음
# 마찬가지로 dp[8]의 1, 3으로 끝난 경우의 수에 2를 더하면 10이 되기 떄문에 두 경우의 수를 더한 값을 dp[10][1]에 넣음
# 마지막으로 dp[7]의 1, 2으로 끝난 경우의 수에 3을 더하면 10이 되기 떄문에 두 경우의 수를 더한 값을 dp[10][2]에 넣음
# dp[10]의 모든 값을 더하면 답을 구할 수 있음.