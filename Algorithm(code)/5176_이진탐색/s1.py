import sys
sys.stdin = open('sample_input.txt')


def in_order(n):
    global a
    if n < N+1:
        in_order(n*2)
        print(n, a)
        temp[n] = a
        a += 1
        in_order(n*2+1)



TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    temp = [0] * (N+1)
    a = 1
    in_order(1)
    print(temp)
    print(f'#{tc}', end=' ')
    print(temp[1], end=' ')
    print(temp[N//2])
