number = set()

for _ in range(10):
    x = int(input())
    y = x % 42
    number.add(y)

print(len(number))