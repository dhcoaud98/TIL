import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # N은 홀수 값이므로 중간값을 구해 middle로 선언
    middle = N // 2

    my_sum = 0
    for i in range(N):
        # 계산할 배열의 행이 middle보다 작거나 같을 경우의 범위
        if i <= middle:
            for k in range(middle-i, middle+i+1):
                my_sum += arr[i][k]
        # 계산할 배열의 행이 middle보다 클 경우의 범위
        else:
            for k in range(i-middle, N+middle-i):
                my_sum += arr[i][k]

    print(f'#{tc} {my_sum}')