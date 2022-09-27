import sys
sys.stdin = open('input.txt')

# dp를 이용?

def f(idy, percentage):  # idy는 현재 행, n은 전체 길이
    global result

    # 마지막에 도달
    if idy == N:
        if percentage > result:
            result = percentage
        return

    # 가지치기
    if result >= percentage:
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] == 1
                new_percentage = percentage * round(arr[idy][i]*0.01, 8)
                f(idy+1, new_percentage)
                visited[i] = 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]
    result = -9999999  # 비교 대상
    percentage = 1  # 계산할 값
    visited = [0] * N

    f(0, 1)
    # 소수점 자리수 제한: f"{1.23456:.2f}" -> 소수점 세번째에서 반올림하여 두번째까지 표현
    print(f'#{tc} {result*100:.6f}')
