a, b = map(int, input().split())

while a != 0 and  b!= 0:
    print("Yes" if a > b else "No")
    a, b = map(int, input().split())
