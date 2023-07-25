doc = input()
word = input()
answer = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break
    else:
        answer += 1
        doc = doc[idx + len(word):]

print(answer)