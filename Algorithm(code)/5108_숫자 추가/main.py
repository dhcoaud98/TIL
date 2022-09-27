import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        now_index, now_value = map(int, input().split())
        row_lst = arr[:now_index]
        row_lst.append(now_value)
        high_lst = arr[now_index:]
        arr = row_lst + high_lst

    print(f'#{tc} {arr[L]}')

