import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 3 5
    # [1, 5, 3] [3, 6, -7, 5, 4]
    # 7 6
    # [6, 0, 5, 5, -1, 1, 6] [-4, 1, 8, 7, -9, 3]
    result = []
    if N <= M:  # A가 B보다 짧을 경우
        for i in range(M-N+1):
            my_sum = 0
            for j in range(N):
                my_sum += A[j] * B[j+i]
            result.append(my_sum)
    if N >= M:  # B가 A보다 짧을 경우
        for i in range(N-M+1):
            my_sum = 0
            for j in range(M):
                my_sum += A[j+i] * B[j]
            result.append(my_sum)

    # 최댓값 출력
    max_num = result[0]
    for i in range(len(result)):
        if result[i] >= max_num:
            max_num = result[i]

    print(f'#{tc} {max_num}')

