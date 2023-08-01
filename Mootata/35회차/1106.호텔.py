c, n = map(int, input().split())  # C명 늘려야 함, 도시의 수
city = [list(map(int, input().split())) for _ in range(n)]
dp = [
    float("inf") for _ in range(c + 100)
]  # 인덱스는 고객의 수 값은 비용, 한번의 홍보로 최대 100명까지 얻을 수 있음
dp[0] = 0

for cost, count in city:
    for i in range(count, c + 100):
        dp[i] = min(dp[i - count] + cost, dp[i])
        # i명을 얻는데 드는 비용과
        # i - count명 까지 얻는데 계산된 최소 비용 + 현재 count명을 얻는데 드는 비용
        # 두 값을 비교하여 더 작은 비용을 dp[i]에 넣음

print(min(dp[c:]))
