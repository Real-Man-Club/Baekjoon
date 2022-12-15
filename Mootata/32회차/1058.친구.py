n = int(input())
friend = []
visit = [[0 for i in range(n)] for i in range(n)]
answer = 0

for i in range(n):
    friend.append(list(input().strip()))

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if friend[i][j] == "Y" or (friend[i][k] == "Y" and friend[k][j] == "Y"):
                    visit[i][j] = 1

floyd()

for i in range(n):
    count = 0
    for j in range(n):
        if visit[i][j] == 1:
            count += 1
    answer = max(answer, count)

print(answer)