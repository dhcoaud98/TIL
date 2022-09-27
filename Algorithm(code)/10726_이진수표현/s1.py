import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())

    binary = bin(M)
    binary = binary[2:].zfill(30)
    end_list = list(binary[30-N:30])

    cnt = 0
    for i in range(len(end_list)):
        if end_list[i] == '1':
            cnt += 1

    if cnt == N:
        result = 'ON'
    else:
        result = 'OFF'

    print(f'#{tc+1} {result}')
