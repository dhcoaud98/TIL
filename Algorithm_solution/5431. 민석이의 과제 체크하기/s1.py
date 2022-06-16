import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [0]*(N+1)
    summit = list(map(int, input().split()))

    # 카운팅 정렬
    for i in range(M):
        arr[summit[i]] += 1

    print(f'#{tc} ', end='')
    temp = []
    for i in range(1, N+1):
        if arr[i] == 0:
            temp.append(i)
    print(*temp)