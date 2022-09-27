import sys
sys.stdin = open('sample_input.txt')


def prim(start, N):  # start는 지작 정점, N은 노드의 개수
    MST = [0] * (N+1)  # 방문 표시를 위해
    MST[start] = 1  # 시작 정점을 방문 표시하기
    ans = 0  # 우리가 구할 값
    for _ in range(N):  # 모든 정점을 탐색하기 위해
        u = 0
        min_value = 10000
        for i in range(N+1):
            if MST[i] == 1:
                for j in range(N+1):
                    if 0 < temp[i][j] < min_value and MST[j] == 0:  # 모든 줄에서 연결되어 있으면서 가중치가 가장 작은 값 찾기
                        u = j
                        min_value = temp[i][j]

        """
        [0, 9, 3, 7, 0],   u = 2, min_value = 3, ans = 3
        [9, 0, 0, 0, 2],   u = 4, min_value = 2, ans = 5
        [3, 0, 0, 8, 1],   u = 1, min_value = 1, ans = 6
        [7, 0, 8, 0, 8],   u = 0, min_value = 7, ans = 13
        [0, 2, 1, 8, 0]
        """
        ans += min_value
        MST[u] = 1
        # print(ans)

    return ans


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    temp = [[0] * (N+1) for _ in range(N+1)]
    # 무방향 인접 행렬 만들기
    for _ in range(M):
        s, e, w = map(int, input().split())
        temp[s][e] = w
        temp[e][s] = w

    print(f'#{tc} {prim(0, N)}')
    