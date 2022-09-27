import sys
import time


sys.stdin = open('s_input.txt')

TC = int(input())
start = time.time()

def f(NUM):
    n = str(NUM)
    for k in range(len(n)-1):
        if int(n[k]) > int(n[k + 1]):  # 단조 아님
            return -1
    return 1

for tc in range(1, TC+1):

    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 두개의 수를 골라 곱한 값 구하기
    max_num = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if f(num) == 1 and num >= max_num:
                max_num = num
    print(f'#{tc} {max_num}')
    print(time.time() - start)



