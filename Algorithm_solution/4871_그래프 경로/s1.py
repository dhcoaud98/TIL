import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

# 경로를 탐색할 함수
def load(s, e):
    global arr, V, stack
    visited = [0] * (V+1)
    i = s  # 재귀에 의해 불려온 s값을 현재 시작점으로 바꿈
    visited[s] = 1  # 1이된 곳은 방문한 곳
    stack.append(s)


    for w in range(1, V+1):
        # 인접한 상태이면서 방문하지 않았다면
        if arr[i][w] == 1 and visited[w] == 0:
            load(w, e)


for tc in range(1, TC+1):
    V, E = map(int, input().split())  # 정점, 간선
    P = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    # print(V, E)
    # print(P)
    # print(start, end)
    # print(arr)
    stack = []

    # 1. 단방향성 인접행렬 만들기
    for i in  range(E):
        n1, n2 = P[i][0], P[i][1]
        arr[n1][n2] = 1

    print(f'#{tc} ', end='')
    load(start, end)
    # 경로에 도달하는지 판별
    if end in stack:
        print(1)
    else:
        print(0)
