import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    arr = list(map(int, input().split()))

    result = 0  # 결과값
    max_i = 0  # 최댓값을 가진 인덱스
    s = 0  # 지금 시작 위치

    while s < N:
        max_i = s
        # 1. 최댓값 찾기
        for i in range(s, N):
            if arr[i] >= arr[max_i]:
                max_i = i
        # 2. 값 계산하기
        for i in range(s, max_i):
            result += arr[max_i] - arr[i]

        s = max_i + 1

    print(f'#{tc} {result}')
