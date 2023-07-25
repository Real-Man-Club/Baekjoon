n = int(input())
num = list(map(int, input().split()))

for i in range(n - 1, 0, -1):  # 뒤에서부터 체크
    if num[i] < num[i - 1]:  # 이전 값이 더 큰 값을 찾음(오름차순이 아니게 되는 부분) = x
        for j in range(n - 1, 0, -1):  # 뒤에서부터
            if num[j] < num[i - 1]:  # x보다 작은 값이 나오면
                num[j], num[i - 1] = num[i - 1], num[j]  # 두 값을 바꾸고
                num = num[:i] + sorted(num[i:], reverse=True)  # x 이전은 내림차순으로 정렬
                print(*num)
                exit(0)

print(-1)
