a, b, c = sorted(map(int, input().split()))

if a == c:
    print(10000 + (a * 1000))
elif a == b or b == c:
    print(1000 + (b * 100))
else:
    print(max(a, b, c) * 100)