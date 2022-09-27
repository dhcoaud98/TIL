import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0]*N

    # 1. 버블 내림차순 정렬
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(N-1):
        for j in range(N-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # [10, 0, 9, 0, 8, 0, 7, 0, 6, 0]
    for i in range(0, len(arr), 2):
        temp[i] = arr[i//2]

    # 2. 버블 오름차순 정렬
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(N-1):
        for j in range(N-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    for i in range(1, len(arr), 2):
        temp[i] = arr[i//2]

    # 3. 출력 (list -> int로)
    print(f'#{tc}', end=' ')
    for i in range(0, 10):
        print(temp[i], end=' ')
    print()


