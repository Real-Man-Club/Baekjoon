for _ in range(int(input())):
    print(*[i for i, x in enumerate(bin(int(input()))[::-1]) if x == '1'])