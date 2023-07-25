a, b = map(int, input().split())
aset = set(map(int, input().split()))
bset = set(map(int, input().split()))

print(len(aset - bset) + len(bset - aset))