import sys
sys.stdin=open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    result = N*M
    cnt = 0
    # 1. 첫 번째 W, 마지막 R로 변경
    for m in range(M):
        if arr[0][m] != 'W':
            cnt += 1
        if arr[N-1][m] != 'R':
            cnt += 1
    cnt = cnt
    # 2. blue의 위치 정해주기
    table = []
    for i in range(1, N - 1):
        temp = [0] * (N - 2)
        for j in range(0, N - 1 - i):
            temp = [0] * (N - 2)
            for k in range(j, j + i):
                temp[k] = 'B'
            table.append(temp)

    # 3. 'B' 이전은 'W', 'B' 이후는 'R'
    for t in table:
        l = 0
        while t[l] != 'B':
            t[l] = 'W'
            l += 1
        l = N-3
        while t[l] != 'B':
            t[l] = 'R'
            l -= 1

    for t in table:
        cnt_2 = 0
        for i in range(N-2):
            for j in range(M):
                if arr[i+1][j] != t[i]:
                    cnt_2 += 1
        if cnt+cnt_2 <= result:
            result = cnt+cnt_2


    print(f'#{tc} {result}')
