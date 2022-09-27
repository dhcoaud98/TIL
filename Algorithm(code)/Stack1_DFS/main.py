import sys
sys.stdin=open('input.txt')

# 2. 경로 찾는 함수
def load(a, V):
    global temp, visited
    visited[a] = 1
    print(f'{a} ', end='')

    for w in range(1, V+1):
        if visited[w] == 0 and temp[a][w] == 1:  # 우선 w라는 정점에 간적이 없고, 인접 행렬 temp의 지정위치가 1이라면
            load(w, V)


# 1. main
# 1-1. 인풋 받기
V, E = map(int, input().split())  # V는 정점의 갯수, E는 경로 갯수
arr = list(map(int, input().split()))

# 1-2. 무방향 인접 행렬 만들기
temp = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[2*i], arr[2*i+1]
    temp[n1][n2] = 1
    temp[n2][n1] = 1

# 1-3. 함수 선언 (시작점, 정점 갯수)
visited = [0] * (V + 1)
load(1, V)
