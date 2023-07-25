from itertools import combinations

n = int(input())
answer = []

for i in range(1, 11):  # 9876543210 = 10자리
    for com in combinations(
        map(str, range(0, 10)), i
    ):  # 0 ~ 9 까지의 str값으로 구성된 i 자리의 조합 튜플 com 생성
        value = int("".join(sorted(com, reverse=True)))  # 감소하는 숫자로 변환
        answer.append(value)

answer.sort()

try:
    print(answer[n])
except:
    print(-1)
