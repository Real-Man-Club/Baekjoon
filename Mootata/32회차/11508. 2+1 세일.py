n = int(input())
c = [int(input()) for _ in range(n)]
c.sort(reverse = True)

answer = 0

for i in range(2, len(c), 3):
    answer += c[i]

print(sum(c) - answer)