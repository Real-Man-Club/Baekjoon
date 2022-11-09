paper = [[0 for _ in range(101)] for _ in range(101)]
answer= 0

for n in range(int(input())):
    a, b = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] = 1

for i in paper:
    answer += sum(i)

print(answer)