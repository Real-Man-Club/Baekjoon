n = int(input())
member = []

for _ in range(n):
    age, name = input().split()
    member.append((int(age), name))

for a, n in sorted(member, key = lambda x: x[0]):
    print(a, n)