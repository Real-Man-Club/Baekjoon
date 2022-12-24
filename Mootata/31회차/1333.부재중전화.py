n, l, d = map(int, input().split())

time = n * l + (n - 1) * 5
song = [False for _ in range(time)]

for i in range(0, time, l + 5):
    for j in range(i, i + l):
        song[j] = True

for i in range(0, time, d):
    if not song[i]:
        print(i)
        break
else:
    print(i + d)