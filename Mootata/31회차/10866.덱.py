from collections import deque
import sys

input = sys.stdin.readline

dq = deque()

for n in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)