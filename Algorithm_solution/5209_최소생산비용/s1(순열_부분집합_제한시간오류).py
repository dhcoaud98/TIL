import sys

sys.stdin = open('sample_input.txt')


def f(n, k):  # 순열 p[n]을 채우는 함수, k 배열의 크기
    global result

    if n == k:
        if my_sum(p) <= result:
            result = my_sum(p)
        # print(result)
    for i in range(k):  # used에서 사용하지 않은 숫자 검색
        if used[i] == 0:  # 앞에서 사용하지 않은 숫자인 경우
            used[i] = 1  # 사용함으로 표시
            p[n] = a[i]  # p[n]결정
            f(n+1, k)
            used[i] = 0  # a[i]를 다른 위치에서 사용할 수 있도록 함
    return


def my_sum(lst):
    # print(lst)
    number = 0
    for k in range(N):
        if number <= result:
            number += arr[k][lst[k]]
    return number

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')

    a = [i for i in range(N)]
    used = [0] * N
    p = [0] * N
    f(0, N)

    print(f'#{tc} {result}')