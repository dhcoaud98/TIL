import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90, 180, 270으로 만들기
    temp_90 = ''
    temp_180 = ''
    temp_270 = ''

    for i in range(N):
        for j in range(N-1, -1, -1):
            temp_90 += str(arr[j][i])

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            temp_180 += str(arr[i][j])

    for i in range(N - 1, -1, -1):
        for j in range(N):
            temp_270 += str(arr[j][i])

    # 출력
    now = 0
    print(f'#{tc} ')
    for i in range(N):
        answer = ''
        answer += str(temp_90[now:now+N]) + ' '
        answer += str(temp_180[now:now+N]) + ' '
        answer += str(temp_270[now:now+N])
        now += N
        print(answer)
        
