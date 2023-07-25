n = int(input())
values = list(map(int, input().split()))
min_val = values[0]
answer = 0

for v in values:
    if min_val < v:
        answer = max(answer, v - min_val)
    else:
        min_val = v

print(answer)

# 날짜별 주가를 확인하여 min_val보다 값이 크면, 이득을 볼 수 있다는 뜻이므로 answer 초기화
# min_val보다 값이 작다면 해당 가격으로 구매하는 것이 더 큰 이득을 볼 수 있으므로 min_val 초기화
