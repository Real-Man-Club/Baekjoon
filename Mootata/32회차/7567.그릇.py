plate = input()
answer = 10
pre = plate[0]

for p in plate[1:]:
    if p == pre:
        answer += 5
    else:
        answer += 10
    pre = p

print(answer)