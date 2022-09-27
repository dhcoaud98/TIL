import sys
sys.stdin = open('input.txt')

def DFS(j, i):
    global min_xy, max_num, answer
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0] * (N) for _ in range(N)]
    visited[j][i] = 1
    queue = []
    queue.append((j, i))

    while queue:
        q = queue.pop(0)
        for k in range(4):
            now_x = q[1] + dx[k]
            now_y = q[0] + dy[k]
            if 0 <= now_x < N and 0 <= now_y < N and arr[now_y][now_x] == arr[q[0]][q[1]] + 1:
                visited[now_y][now_x] = visited[q[0]][q[1]] + 1  # 방문표시하면서 연속으로 몇번째인지 기록
                queue.append((now_y, now_x))
                if visited[now_y][now_x] >= max_num:
                    max_num = visited[now_y][now_x]
                    answer.append([arr[j][i], max_num])

    return max_num, answer


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = (0, 0)
    answer = []
    max_num = 1
    min_xy = N*N
    visited = [[0] * (N) for _ in range(N)]
    
    # DFS를 통해 갈 수 있는 모든 경로 찾기
    for i in range(N):
        for j in range(N):
            DFS(j, i)
    
    # 최대 거리에서 가장 작은 시작 값 찾기
    for m in range(len(answer)):
        if answer[m][1] == max_num:
            if answer[m][0] < min_xy:
                min_xy = answer[m][0]

    print(f'#{tc} {min_xy} {max_num}')

