import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 오름차순 정렬
    for j in range(N-1):
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(f'#{tc}', end =' ')
    for k in arr:
        print(k, end=' ')
    print()