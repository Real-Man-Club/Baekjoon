n = int(input())
p1, p2 = 0, 1 # dp 배열 없이
for i in range(n):
    p1, p2 = p2, p1+p2
print(p1)
