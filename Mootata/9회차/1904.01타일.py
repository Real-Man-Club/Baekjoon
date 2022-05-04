n = int(input()) # 길이 n
dp = [0, 1, 2, 3, 5]

for i in range(5, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 15746)

print(dp[n])

# n = 1, 1 1
# n = 2, 2 00, 11
# n = 3, 3 001 100 111
# n = 4, 5 0011, 0000, 1001, 1100, 1111
# n = 5, 8 00001, 00100, 10000, 00111, 11001, 10011, 00111, 11111