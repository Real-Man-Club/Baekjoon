for t in range(int(input())):
    result = input()
    answer = 0
    score = 0
    
    for i in result:
        if i == 'O':
            score += 1
            answer += score
        else:
            score = 0
    
    print(answer)