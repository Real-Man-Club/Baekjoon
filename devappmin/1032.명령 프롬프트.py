print(*[x[0] if len(set(x))==1 else '?' for x in zip(*list(input()for _ in range(int(input()))))],sep='')
