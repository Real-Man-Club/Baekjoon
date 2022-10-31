n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

graph.sort(key = lambda x: (x[0], x[1]))

for i in graph:
    print(*i)