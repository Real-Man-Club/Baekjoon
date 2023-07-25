from math import gcd

for t in range(int(input())):
    number = list(map(int, input().split()))
    answer = 0
    
    for i in range(1, len(number)):
        for j in range(i + 1, len(number)):
            answer += gcd(number[i], number[j])

    print(answer)