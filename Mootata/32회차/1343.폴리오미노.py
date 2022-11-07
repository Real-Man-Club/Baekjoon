board = input()
answer = []
count = 0

def appends():
    b = count % 4
    a = count - b
    for _ in range(a):
        answer.append('A')
    for _ in range(b):
        answer.append('B')

def check():
    if count % 2 == 1:
        return True
    else:
        return False

for i in board:
    if i == 'X':
        count += 1
    elif i == '.':
        if check():
            print(-1)
            exit(0)
        appends()
        answer.append('.')
        count = 0

if count != 0:
    if check():
        print(-1)
        exit(0)
    appends()

print(*answer, sep='')