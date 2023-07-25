import enum


n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse = True)
answer = 0

for idx, tip in enumerate(tips):
    t = tip - idx
    
    if t > 0:
        answer += t

print(answer)