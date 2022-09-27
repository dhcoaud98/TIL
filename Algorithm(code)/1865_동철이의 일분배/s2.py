import sys
sys.stdin = open('input.txt')


def f(idx, result):  # idx는 현재 행, n은 전체 길이
    global max_result

    # 마지막에 도달
    if idx == N:
        if result > max_result:
            max_result = result
        return

    # 가지치기
    if result <= max_result:
        return

    for i in range(N):
        if visited[i] == 0:  # 방문하지 않았다면
            visited[i] = 1
            new_result = result*arr[idx][i]*0.01
            f(idx+1, new_result)
            visited[i] = 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]
    max_result = -9999999
    visited = [0] * N

    f(0, 1)
    # 소수점 자리수 제한: f"{1.23456:.2f}" -> 소수점 세번째에서 반올림하여 두번째까지 표현
    print(f'#{tc} {max_result*100:.6f}')
