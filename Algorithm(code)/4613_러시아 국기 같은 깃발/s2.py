import sys
sys.stdin=open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    print(arr)
    cnt = 0
    # 1. 첫째 줄은 W
    for i in range(M):
        if arr[0][i] == 'B' or arr[0][i] == 'R':
            cnt += 1

    # 2. 마지막 줄은 R
    for i in range(M):
        if arr[N-1][i] == 'W' or arr[N-1][i] == 'W':
            cnt += 1

    # 3. 중간 부분
    # N-2 = white + blue + red
    # 4 = white + blue + red
    a = b = c = 0
    temp = [a, b, c]
    result = []
    for i in range(N-2, -1, -1):





