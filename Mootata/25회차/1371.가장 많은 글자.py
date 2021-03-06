import sys
from collections import defaultdict

s = sys.stdin.read()
dic = defaultdict(int)
answer = []

for i in s:
    if i.isalpha():
        dic[i] += 1

max_val = dic.get(max(dic, key=dic.get)) # 가장 큰 값을 찾음

for key, value in dic.items():
    if value == max_val:
        answer.append(key)

print(*sorted(answer), sep='')
