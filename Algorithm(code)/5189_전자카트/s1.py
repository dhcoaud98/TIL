import sys
sys.stdin = open('sample_input.txt')


def pick(n, k):  # 길정해주기
    global result
    if n == k:
        # print(p)
        if battery(p) <= result:
            result = battery(p)

    else:
        for i in range(1, k):
            if used[i] == 0:
                used[i] = 1
                p[n] = temp[i-1]
                pick(n+1, k)
                used[i] = 0

    return result

def battery(lst):
    # print(lst)
    total = 0
    for i in range(len(lst)-1):
        if total <= result:
            total += arr[lst[i]][lst[i+1]]
        else:
            break
    return total


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 1에서 출발해서 1로 돌아옴
    """
    N = 3인 경우
    1-2-3-1
    1-3-2-1
    2, 3으로 순열
    
    N = 4인 경우
    1-2-3-4-1
    1-2-4-3-1
    1-3-2-4-1
    1-3-4-2-1
    1-4-2-3-1
    1-4-3-2-1
    2, 3, 4 로 순열
    """
    result = 1000
    temp = [i for i in range(2, N+1)]
    used = [1] + [0] * len(temp) + [1]
    p = [1] + [0] * len(temp) + [1]
    print(f'#{tc} {pick(1, N)}')
