print("Gnomes:")
for _ in range(int(input())):
    li = list(map(int, input().split()))
    print("Ordered" if li == sorted(li) or li == sorted(li)[::-1] else "Unordered")
