num = input()
pre = num[0]
answer = 1

for i in num[1:]:
    if i != pre:
        answer += 1
        pre = i

print(answer // 2)