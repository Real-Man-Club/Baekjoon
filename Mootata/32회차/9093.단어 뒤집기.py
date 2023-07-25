for t in range(int(input())):
    string = input().split()
    for s in string:
        print(s[::-1], end = ' ')