w = 0
for _ in range(6):
    if input() == 'W':
        w += 1

if 5 <= w <= 6:
    print(1)
elif 3 <= w <= 4:
    print(2)
elif 1 <= w <= 2:
    print(3)
else:
    print(-1)
