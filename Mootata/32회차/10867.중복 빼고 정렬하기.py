n = int(input())
number = list(set(map(int, input().split())))

print(*sorted(number))