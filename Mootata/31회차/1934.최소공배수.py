from math import gcd

for t in range(int(input())):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))