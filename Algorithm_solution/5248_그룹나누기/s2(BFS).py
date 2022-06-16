import sys
sys.stdin = open('sample_input(8).txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = [[0]*(N+1) for _ in range(N+1)]

    # 무방향 인접 리스트 만들기
    for i in range(M):
        temp[lst[i*2]][lst[i*2+1]] = 1
        temp[lst[i*2+1]][lst[i*2]] = 1
    """
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    """

    visited = [0] * (N + 1)
    queue = []
    ans = 0
    for j in range(1, N+1):
        if visited[j] == 0:  # 방문한 기록이 없을 경우에만!
            queue.append(j)
            while queue:
                q = queue.pop(0)
                visited[q] = 1  # 방문표시하기
                for i in range(1, N+1):
                    if temp[q][i] == 1 and visited[i] == 0:
                        queue.append(i)

            ans += 1

    print(f'#{tc} {ans}')
