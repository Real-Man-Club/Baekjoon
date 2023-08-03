from collections import deque, defaultdict

n, k = map(int, input().split())
per = tuple(map(int, input().split()))
s = tuple(sorted(per))
visited = defaultdict(bool)


def bfs():
    q = deque([(per, 0)])

    while q:
        p, count = q.popleft()
        visited[p] = True
        if p == s:
            return count

        for i in range((n + 1) - k):
            np = p[:i] + tuple(reversed(p[i : i + k])) + p[i + k :]

            if visited[np]:
                continue
            q.append((np, count + 1))
            visited[np] = True

    return -1


print(bfs())
