from collections import deque
import sys

input = sys.stdin.readline

q = deque()

for n in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)