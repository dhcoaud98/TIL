import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    q = 0

    # 1. 가로
    for i in range(9):
        for j in range(1, 10):
            if j in arr[i]:
                result += 1
    if result == 81:
        q = q + 1

    # 2. 정사각형
    row = result = 0
    words = []
    for i in range(3):
        col = 0
        while col < 9:
            for j in range(3):
                for k in range(3):
                    words.append(arr[j+row][k+col])
            col += 3
        row += 3

    now = 0
    for i in range(9):
        for m in range(1, 10):
            if m in words[0+now:9+now]:
                result += 1
        now += 9
    if result == 81:
        q = q + 1

    # 3. 세로
    # 전치
    result = 0
    arr = list(map(list, zip(*arr)))

    for i in range(9):
        for j in range(1, 10):
            if j in arr[i]:
                result += 1
    if result == 81:
        q = q + 1

    # 4. 결과
    if q == 3:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')