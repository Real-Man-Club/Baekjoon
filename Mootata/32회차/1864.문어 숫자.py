while True:
    oc_num = list(input())
    
    if oc_num[0] == '#':
        break
    
    answer = 0
    idx = len(oc_num) - 1
    
    for i in oc_num:
        if i == '-':
            answer += 0
        elif i == '\\':
            answer += 8 ** idx
        elif i =='(':
            answer += 2 * (8 ** idx)
        elif i == '@':
            answer += 3 * (8 ** idx)
        elif i == '?':
            answer += 4 * (8 ** idx)
        elif i == '>':
            answer += 5 * (8 ** idx)
        elif i == '&':
            answer += 6 * (8 ** idx)
        elif i == '%':
            answer += 7 * (8 ** idx)
        elif i == '/':
            answer += -1 * (8 ** idx)
        
        idx -= 1
    
    print(answer)