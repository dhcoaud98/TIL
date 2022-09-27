import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # N개의 원소, 부분집합의 합 K
    N, K = map(int, input().split())
    n = 12

    arr = []
    result = 0

    for i in range(1, n+1):
        arr.append(i)

    # 부분집합 모두 구해서 total에 합을 넣고, cnt에 원소의 갯수 넣기
    for i in range(1 << n):
        total = 0
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                total += arr[j]
                cnt += 1

        if cnt == N and total == K:
            result += 1

    print(f'#{tc} {result}')