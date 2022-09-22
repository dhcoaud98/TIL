import sys
sys.stdin = open('input.txt')


def bt(n, k):
    global answer, result

    if n == k:
        print(result)
        if result not in used:
            used.append(result)
        # if result not in used:
        #     used.append(result)
        #     print("used", used)
            max_dalante = mat(result)
            if max_dalante > answer:
                answer = max_dalante

    else:
        for i in range(P):
            result[i] += 1
            bt(n+1, k)
            result[i] -= 1


def mat(lst):
    total = 1
    for j in range(len(lst)):
        total *= lst[j]
    return total


TC = int(input())
for tc in range(1, 1+1):
    N, P = map(int, input().split())

    used = []
    result = [1] * P
    answer = 0
    dalante = N-P

    bt(0, dalante)
    print(f'#{tc} {answer}')