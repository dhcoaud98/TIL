import sys
sys.stdin = open('sample_input.txt')

def dijkstra(n):  # 다익스트라 알고리즘
    global cnt
    while cnt < N:
        u = -1
        min_value = float('inf')
        for i in range(N+1):
            if visited[i] == 0 and distance[i] < min_value:
                min_value = distance[i]
                u = i
        visited[u] = 1
        cnt += 1
        for i in range(1, N+1):
            if temp[u][i] != 0:
                if distance[i] > distance[u] + temp[u][i]:
                    distance[i] = distance[u] + temp[u][i]
        """
        [0, 1, 6]
        [0, 1, 2]
        """
    return distance


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    temp = [[0]*M for _ in range(M)]

    for m in range(M):
        s, e, w = map(int, input().split())
        temp[s][e] = w
    """
    [0, 1, 6],
    [0, 0, 1], 
    [0, 0, 0]
    """
    visited = [0 for _ in range(N+1)]
    distance = [float('inf') for _ in range(N+1)]
    distance[0] = 0
    cnt = 0

    print(f'#{tc} {dijkstra(0)[N]}')
