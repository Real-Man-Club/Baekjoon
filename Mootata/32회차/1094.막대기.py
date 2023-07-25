x = int(input())
sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in sticks:
    if x >= i:
        count += 1
        x -= i
print(count)