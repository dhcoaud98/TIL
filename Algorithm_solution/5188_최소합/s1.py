import sys
sys.stdin = open('sample_input.txt')

"""
1 0
2 0
3 0
3 1
3 2
3 3
30
2 1
3 1
3 2
3 3
26
2 2
3 2
3 3
26
2 3
1 1
2 1
3 1
3 2
3 3
18
2 2
3 2
3 3
18
2 3
1 2
2 2
1 3
2 3
0 1
1 1
2 1
3 1
3 2
3 3
21
...
"""

def min_sum(si, sj):  # DFS로 풀기
    global load_sum, result

    if load_sum >= result:  # 가지치기(계산 하던 도중 최소값보다 크면 종료)
        return

    stack = [(si, sj)]
    q = stack.pop()
    for k in range(2):  # 하, 우
        ni = q[0] + dy[k]
        nj = q[1] + dx[k]
        if 0 <= ni < N and 0 <= nj < N:
            stack.append((ni, nj))
            load_sum += arr[ni][nj]

            if ni == ei and nj == ej:
                if load_sum <= result:  # result에 작은 값만 넣기
                    result = load_sum
                load_sum -= arr[ni][nj]
                return
            min_sum(ni, nj)
            load_sum -= arr[ni][nj]  # 돌아온 길의 합은 빼주기


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, 0]  # 하, 우
    dx = [0, 1]

    si, sj = 0, 0
    ei, ej = N-1, N-1
    result = 10*N*N
    load_sum = arr[si][sj]
    min_sum(si, sj)

    print(f'#{tc} {result}')