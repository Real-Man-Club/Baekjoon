n = int(input())
inval = {}
answer = 0

for i in range(n):  # 들어간 차의 순서
    inval[input()] = i

outval = [input() for _ in range(n)]  # 나온 차

for i in range(n - 1):
    for j in range(i + 1, n):
        if (
            inval[outval[i]] > inval[outval[j]]
        ):  # 현재 확인하는 차량보다 먼저 들어간 차량이 있었지만 그 차량보다 먼저 나온 경우 (추월한 경우)
            answer += 1
            break

print(answer)
