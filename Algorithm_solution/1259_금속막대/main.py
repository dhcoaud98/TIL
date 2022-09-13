import sys
sys.stdin = open('input.txt')


def fc(lst):
    for i in range(N):
        if i not in used:
            if result[-1] == arr[2*i]:
                used.append(i)
                lst.append(arr[2 * i])
                lst.append(arr[2 * i + 1])
                fc(lst)

    return lst

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = []

    for n in range(N):
        result, used = [], []
        # used = []
        used.append(n)
        result.append(arr[2*n])
        result.append(arr[2*n+1])
        # print(fc(result))  # 시작 수나사, 시작 암나사
        if len(fc(result)) > len(answer):
            answer = fc(result)

    print(f'#{tc}', *answer)