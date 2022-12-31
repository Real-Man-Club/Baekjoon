for t in range(int(input())):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    for n in note2:
        if n in note1:
            print(1)
        else:
            print(0)