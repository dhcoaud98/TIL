import sys
sys.stdin = open('input.txt')

# 함수
def load(s, e):
    global visited, stack, V
    i = s
    visited[s] = 1

    for w in range(0, V):
        if visited[w] == 0 and arr[i][w] == 1:
            load(w, 99)
            stack.append(w)

# 메인
for tc in range(1, 11):
    V = 100  # 정점의 갯수
    t, E = map(int, input().split())
    P = list(map(int, input().split()))


    # 단방향 인접 행렬 만들기
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2 = P[2*i], P[2*i+1]
        arr[n1][n2] = 1

    stack = []
    visited = [0] * (V+1)
    load(0, 99)
    print(f'#{tc}', end=' ')
    if 99 in stack:
        print(1)
    else:
        print(0)