word = list(input())
results = []
n = len(word)

for i in range(1, n - 1):
    for j in range(i + 1, n):
        results.append(''.join(list(reversed(word[0:i])) + list(reversed(word[i:j])) + list(reversed(word[j:]))))

print(sorted(results)[0])