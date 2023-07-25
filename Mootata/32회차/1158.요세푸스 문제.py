n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
answer = []
idx = k - 1

while people:
    idx = idx % len(people)
    answer.append(people.pop(idx))
    idx += k - 1

print('<', end='')
print(*answer, sep=', ', end='')
print('>')