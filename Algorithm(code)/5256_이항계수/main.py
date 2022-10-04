import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    n, a, b = map(int, input().split())

    temp = [[0 for _ in range(n+1)] for _ in range(n)]
    temp[0][0], temp[0][1] = 1, 1

    for i in range(1, n):
        for j in range(n+1):
            if j == 0:
                temp[i][j] = 1
            else:
                temp[i][j] = temp[i-1][j] + temp[i-1][j-1]

    print(f'#{tc} {temp[n-1][a]}')