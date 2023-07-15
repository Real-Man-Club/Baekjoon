from collections import deque

n = int(input())
eggs = [list(map(int, input().split())) for i in range(n)]
q = deque([eggs[0], 0])
answer = 0


def check(eggs):
    count = 0
    for e in eggs:
        if e[0] <= 0:
            count += 1
    return max(answer, count)


def dfs(idx, eggs):
    global answer
    if idx == n:  # 마지막 계란
        answer = check(eggs)
        return

    if eggs[idx][0] <= 0:  # 선택된 계란이 깨져있을 때는 다음 계란으로
        dfs(idx + 1, eggs)
        return

    for i, e in enumerate(eggs):
        if i == idx:
            continue
        if e[0] > 0:
            break
    else:  # 모든 계란이 깨져있을 때
        answer = check(eggs)
        return

    for i in range(n):
        if i == idx or eggs[i][0] <= 0:
            continue

        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        dfs(idx + 1, eggs)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]


dfs(0, eggs)
print(answer)
