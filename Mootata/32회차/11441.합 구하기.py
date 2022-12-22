import sys

input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
m = int(input())
sums = [0, number[0]]

for i in range(1, len(number)):
    sums.append(sums[i] + number[i])

for k in range(m):
    i, j = map(int, input().split())
    print(sums[j] - sums[i - 1])