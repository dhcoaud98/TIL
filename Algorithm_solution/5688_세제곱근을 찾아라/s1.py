import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    if round(N**(1/3), 2) % 1 == 0:
        print(f'#{tc} {int(round(N**(1/3), 1))}')
    else:
        print(f'#{tc} {-1}')
