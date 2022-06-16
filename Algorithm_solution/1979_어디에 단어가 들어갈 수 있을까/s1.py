import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N_K = list(map(int, input().split()))
    N = N_K[0]
    K = N_K[1]
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 1. 가로로 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1:  # 값이 0 이거나 현재 열이 마지막일때, cnt의 값이 K와 같은지 비교
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
                    
    # 세로로 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0

    print(f'#{tc} {result}')





