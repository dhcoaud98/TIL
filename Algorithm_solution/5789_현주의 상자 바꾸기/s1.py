import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, Q = map(int, input().split())

    temp = [0] * (N+1)

    print(f'#{tc}', end=' ')

    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            temp[i] = q

    print(*temp[1:N+1])


