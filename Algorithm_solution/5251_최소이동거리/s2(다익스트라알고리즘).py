import sys
sys.stdin = open('sample_input.txt')


TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V + 1)}

    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
    print(adj)
    
    INF = float('inf')
    dist = [INF] * (V + 1)
    selected = [False] * (V + 1)  # 방문표시

    dist[0] = 0
    cnt = 0
    while cnt < V:
        min = INF
        u = -1
        for i in range(V + 1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1

        for w, cost in adj[u]:  # 도착정점, 가중치
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print(f'#{tc} {dist[V]}')