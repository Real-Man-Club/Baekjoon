s = input()
postfixes = []

for i in range(len(s)):
    postfixes.append(s[i:])

print(*sorted(postfixes), sep = '\n')