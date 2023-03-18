# print(*[sum(map(int,x.split())) for x in open(0)[1:]],sep='\n')
for _ in range(int(input())):print(sum(map(int,input().split())))
