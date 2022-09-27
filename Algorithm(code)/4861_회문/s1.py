import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = []
    # 1. 가로로 풀기
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):  # M의 반 만큼 비교
                if arr[i][j+k] != arr[i][-1-k]:
                    break
                if k == M//2 - 1:
                    result = arr[i][j:j+M]

    # 2. 세로로 풀기
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):  # M의 반 만큼 비교
                if arr[j+k][i] != arr[-1-k][i]:
                    break
                if k == M//2 - 1:
                    for m in range(M):
                        result.append(arr[j+m][i])

    print(f'#{tc} ' + ''.join(result))


