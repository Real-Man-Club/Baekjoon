n = int(input())
student = []

for i in range(n):
    name, k, e, m = input().split()
    student.append((int(k), int(e), int(m), name))

student.sort(key = lambda x: (-x[0], x[1], -x[2], x[3]))

for _, _, _, name in student:
    print(name)