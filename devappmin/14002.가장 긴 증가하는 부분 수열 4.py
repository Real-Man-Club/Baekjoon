import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n + 1)

for i_idx in range(len(nums)):
    for j_index in range(i_idx):
        if nums[j_index] < nums[i_idx]:
            dp[i_idx] = max(dp[i_idx], dp[j_index] + 1)

temp = max(dp)
print(temp)

answer = []
for i_idx in range(n - 1, -1, -1):
    if dp[i_idx] == temp:
        answer.append(nums[i_idx])
        temp -= 1

answer = answer[::-1]
print(*answer)
