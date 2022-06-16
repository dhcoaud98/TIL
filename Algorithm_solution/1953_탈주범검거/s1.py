import sys
sys.stdin = open('sample_input.txt')


def load(r, c):
    queue = []
    cnt = 1
    queue.append([r, c])
    while queue:
        q = queue.pop(0)
        pipe_direction = pipe[arr[q[0]][q[1]]]

        if pipe_direction[0] == 1:  # 상
            if 0 <= q[0]-1 < N and 0 <= q[1] < M and visited[q[0]-1][q[1]] == 0 and arr[q[0]-1][q[1]] in [1, 2, 5, 6]:
                visited[q[0] - 1][q[1]] = visited[q[0]][q[1]] + 1
                if visited[q[0]-1][q[1]] == L+1:
                    break
                queue.append((q[0]-1, q[1]))
                cnt += 1

        if pipe_direction[1] == 1:  # 하
            if 0 <= q[0]+1 < N and 0 <= q[1] < M and visited[q[0]+1][q[1]] == 0 and arr[q[0]+1][q[1]] in [1, 2, 4, 7]:
                visited[q[0] + 1][q[1]] = visited[q[0]][q[1]] + 1
                if visited[q[0]+1][q[1]] == L+1:
                    break
                queue.append((q[0]+1, q[1]))
                cnt += 1

        if pipe_direction[2] == 1:  # 좌 (1345)
            if 0 <= q[0] < N and 0 <= q[1]-1 < M and visited[q[0]][q[1]-1] == 0 and arr[q[0]][q[1]-1] in [1, 3, 4, 5]:
                visited[q[0]][q[1] - 1] = visited[q[0]][q[1]] + 1
                if visited[q[0]][q[1] - 1] == L+1:
                    break
                queue.append((q[0], q[1]-1))
                cnt += 1

        if pipe_direction[3] == 1:  # 우
            if 0 <= q[0] < N and 0 <= q[1]+1 < M and visited[q[0]][q[1]+1] == 0 and arr[q[0]][q[1]+1] in [1, 3, 6, 7]:
                visited[q[0]][q[1] + 1] = visited[q[0]][q[1]] + 1
                if visited[q[0]][q[1]+1] == L+1:
                    break
                queue.append((q[0], q[1]+1))
                cnt += 1

    return cnt


TC = int(input())
for tc in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    # 파이프 번호에 따라 갈 수 있는 곳 만들기
    pipe = [[0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]

    visited[R][C] = 1
    print(f'#{tc}', end=' ')
    print(load(R, C))

