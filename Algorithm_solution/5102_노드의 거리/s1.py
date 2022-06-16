import sys
sys.stdin = open('sample_input.txt')

def parent(end):
    queue = []
    visited = [0] * (N+1)
    queue.append(end)
    visited[end] = 1

    while queue:  # 모든 정점이 방향성 없이 이어져 있으므로 모든 노드를 탐색
        p = queue.pop(0)
        for j in range(1, N+1):
            if ch[j][p] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = visited[p] + 1

    if visited[start] != 0:
        return visited[start]-1
    else:
        return 0

TC = int(input())
for tc in range(1, TC+1):
    N, E = map(int, input().split())
    ch = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        q, c = map(int, input().split())
        ch[q][c] = 1
        ch[c][q] = 1
    start, end = map(int, input().split())
    # 자식으로부터 부모 노드 찾아가기

    # print(ch)
    # print(start, end)
    print(f'#{tc} {parent(end)}')
