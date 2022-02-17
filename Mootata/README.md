## 구간 합 구하기

구간 합은 누적 합을 이용해서 구할 수 있음. 예를들어 a ~ b 사이의 구간 합을 구하려고 할 때,  
첫번째 수부터 b번째 수까지 더한 값에서 첫번째 수부터 a - 1번째 수까지 더한 값을 뺴준 것과 같음  
따라서 리스트에 각 인덱스까지의 누적합을 담아두고, list[b] - list[a - 1] 로 a ~ b까지의 구간 합을 구할 수 있음.

## 플로이드-워셜

플로이드-워셜 알고리즘은 모든 노드에서 모든 노드까지의 최단거리를 구하는 방법임

```python
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```

위의 코드가 플로이드-워셜의 키가 되는 코드라고 보면 되는데, graph[x][y]에는 x에서 y로 가는 비용이 담겨있음.

```python
graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```

이 부분을 보면 결국 i에서 j로 바로가는 비용과 i에서 k로 가고, k에서 j로 가는 비용을 더한 값을 비교해서 더 작은 값으로 비용을 업데이트 해주는 것임 이것을 반복해서 결국에는 각 노드에서 모든 노드로 가는 최단거리를 구할 수 있음

## BFS를 이용하여 구역의 수 구하기

2667.단지번호붙이기, 10026.적록색약 등의 문제 처럼 그래프에서 어떤 규칙을 가진 구역의 수를 구할 때

```python
for i in range(n):
    for j in range(n):
        if not visited[i][j] and 특정 조건(ex)단지번호붙이기. graph[i][j] == 1):
            bfs(i, j)
            count += 1
```

위의 코드처럼 모든 정점을 기준으로 주변을 탐색하는데, 시작지점 (i, j)를 기준으로 인접한 지역을 탐색하므로 한번의 탐색이 끝날 때마다 하나의 구역이 생성된다고 생각하면 됨. 따라서 bfs가 한번 실행 될 때마다 count의 값을 1씩 더해주어 총 몇개의 구역이 생성되는지 구할 수 있음.