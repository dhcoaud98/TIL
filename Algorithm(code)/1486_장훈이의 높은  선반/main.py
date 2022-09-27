import sys
sys.stdin = open('input.txt')


def func(idx, N):
    my_sum = 0
    if idx == N:
        for i in range(N):
            if bit[i] == 1:
                my_sum += cashier[i]
            if my_sum >= B:
                result.append(my_sum)


    else:
        bit[idx] = 0
        func(idx + 1, N)
        bit[idx] = 1
        func(idx + 1, N)


TC = int(input())
for tc in range(1, TC+1):
    N, B = map(int, input().split())
    cashier = list(map(int, input().split()))
    # print(cashier)
    # 부분집합 만들기
    bit = [0] * N
    result = []

    func(0, N)
    print(f'#{tc} {min(result)-B}')
