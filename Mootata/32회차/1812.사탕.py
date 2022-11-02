n = int(input())
candies = []
sum = 0

for i in range(n):
    candy = int(input())
    candies.append(candy)
    sum += candy

sum //= 2

for i in range(n):
    num = 0
    for j in range(1, n, 2):
        num += candies[(i + j) % n]
    print(sum - num)