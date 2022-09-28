import sys
sys.stdin = open('input.txt')


TC = int(input())

for tc in range(1, TC+1):
    N, P = map(int, input().split())
    Q, R = N // P, N % P
    ans = (Q + 1) ** R * Q ** (P - R)

    print(f'#{tc} {ans}')
