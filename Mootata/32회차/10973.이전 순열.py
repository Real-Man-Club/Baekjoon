n = int(input())
number = list(map(int, input().split()))


for i in range(n - 1, 0 , -1):
    if number[i] < number[i - 1]:
        for j in range(n - 1, 0, -1):
            if number[j] < number[i - 1]:
                number[j], number[i - 1] = number[i - 1], number[j]
                number = number[:i] + sorted(number[i:], reverse = True)
                print(*number)
                exit(0)
print(-1)