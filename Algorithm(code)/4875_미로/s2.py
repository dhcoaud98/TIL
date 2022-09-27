import sys


sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]  # 2차원 배열로 받기
    # 요소가 3인 것을 찾은 후 3 위치의 x, y 값을 저장해둠
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                x = i
                y = j

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = []  # 방문 한 지점
    stack = [[x, y]]
    flag = 0

    while stack:
        v = stack.pop()  # 스택의 마지막에 있는 것을 검사
        if v not in visited:  # 방문을 하지 않은 것일면 방문하고
            visited.append(v)
            for k in range(4):  # 그 이후의 길 탐색
                if 0 <= v[0] + dx[k] < N and 0 <= v[1] + dy[k] < N:
                    if arr[v[0] + dx[k]][v[1] + dy[k]] == 2:  # 2를 만났으므로 미로를 찾음
                        flag = 1
                        print(f'#{tc} 1')
                    elif arr[v[0] + dx[k]][v[1] + dy[k]] == 0:  # 다음에 갈 길을 찾은 경우 그 값을 stack에 넣기
                        stack.append([v[0] + dx[k], v[1] + dy[k]])

    # stack이 빌 때까지 while 반복문이 돌았는데 2를 만나지 못한 것이므로 미로를 못 찾은 경우우
    if flag == 0:
        print(f'#{tc} 0')