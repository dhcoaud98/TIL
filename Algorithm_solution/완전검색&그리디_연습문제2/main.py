import sys
sys.stdin = open('input.txt')


def f(n, k, m):  # 순열 p[n]을 채우는 함수, k 고를 개수, m 주어진 숫자 개수
    global result
    run = trip = 0
    baby_gin = 0
    if n == k:
        # 3개 씩 끊어서 계산
        # run?
        for i in range(2):
            half = p[3*i:3*i+3]
            for j in range(2):
                if half[j] == half[j+1] - 1:  # run인지
                    run += 1
                    if run == 2:
                        baby_gin += 1
                if half[j] == half[j+1]:
                    trip += 1
                    if trip == 2:
                        baby_gin += 1

            if baby_gin >= 2:
                result = 'True'

    else:
        for i in range(len(arr)):
            if used[i] == 0:
                used[i] = 1
                p[n] = arr[i]
                f(n+1, k, m)
                used[i] = 0

TC = int(input())
for tc in range(1, TC+1):
    arr = list(map(int, input()))
    result = 'False'
    # 완전 검색 위해 순열 만들고, 계산
    used = [0]*len(arr)
    p = [0]*len(arr)
    f(0, len(arr), len(arr))
    print(result)