import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    weigth = sorted(map(int, input().split()), reverse=True)
    volumn = sorted(map(int, input().split()), reverse=True)

    # print(weigth)
    # print(volumn)
    start = 0
    total = 0
    for i in range(M):
        for j in range(start, N):
            if volumn[i] >= weigth[j]:
                total += weigth[j]
                start = j+1
                break

    print(f'#{tc} {total}')