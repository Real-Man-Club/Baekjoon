answer = [0] * 26

for s in input():
    answer[ord(s) - 97] += 1

print(*answer)