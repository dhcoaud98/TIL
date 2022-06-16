import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(M):
        p = arr.pop(0)
        arr.append(p)

    print(f'#{tc} {arr[0]}')