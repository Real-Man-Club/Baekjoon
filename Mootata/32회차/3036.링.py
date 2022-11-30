from math import gcd

n = int(input())
ring = list(map(int, input().split()))

for r in ring[1:]:
    g = gcd(ring[0], r)
    print('{}/{}'.format(ring[0] // g, r // g))