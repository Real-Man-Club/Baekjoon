import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    answer = 0
    count = 5
    
    while count <= n:
        answer += n // count
        count *= 5
        
    print(answer)