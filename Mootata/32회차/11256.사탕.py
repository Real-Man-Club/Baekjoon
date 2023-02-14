for t in range(int(input())):
    j, n = map(int, input().split())
    box = []
    answer = 0
    
    for i in range(n):
        r, c = map(int, input().split())
        box.append(r * c)
    
    box.sort(reverse=True)
    
    while j > 0:
        j -= box[answer]
        answer += 1
        
    print(answer)