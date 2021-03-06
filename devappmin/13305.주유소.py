import sys

n = int(sys.stdin.readline())

dists = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

ans = 0
minimum = prices[0]
for idx in range(n - 1):
    minimum = min(prices[idx], minimum)
    ans += minimum * dists[idx]

print(ans)
