import sys
sys.stdin = open('sample_input.txt')


"""
p1: [9, 5, 5]
p2: [9, 6, 6]
p1: [9, 5, 5, 1]
p2: [9, 6, 6, 1]
p1: [9, 5, 5, 1, 4]
p2: [9, 6, 6, 1, 2]
p1: [9, 5, 5, 1, 4, 2]
p2: [9, 6, 6, 1, 2, 1]

각각의 p1, p2를 순열로 만든 후 [0:3]까지만 check 함수에서 run 인지 triplet인지 확인!
"""

def permutation(n, k, lst, w):  # 순열 만들기
    if n == k:
        # print(card)
        check(card, w)

    for j in range(k):  # used에서 사용하지 않은 숫자 검색
        if used[j] == 0:  # 앞에서 사용하지 않은 숫자인 경우
            used[j] = 1  # 사용함으로 표시
            card[n] = lst[j]  # p[n]결정
            permutation(n + 1, k, lst, w)
            used[j] = 0  # a[j]를 다른 위치에서 사용할 수 있도록 함
    return


def check(card, w):  # run 인지 triplet 인지
    # run 이나 triplet 이 하나라도 result에 넣기!
    run_cnt = 0
    trip = 0

    for m in range(2):
        if card[m] == card[m+1] + 1:
            run_cnt += 1
            if run_cnt == 2:
                result.append(w)
                break
    for m in range(2):
        if card[m] == card[m+1]:
            trip += 1
            if trip == 2:
                result.append(w)
                break


TC = int(input())
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = []
    for i in range(12):
        if i % 2 == 0:
            p1.append(arr[i])
        else:
            p2.append(arr[i])
    # print(p1, p2)

    for i in range(4):
        # p1 탐색
        play1 = p1[0:3+i]
        used = [0] * len(play1)
        card = [0] * len(play1)
        # print(play1)
        permutation(0, len(play1), play1, 1)
        # p2 탐색
        play2 = p2[0:3+i]
        used = [0] * len(play2)
        card = [0] * len(play2)
        # print(play2)
        permutation(0, len(play2), play2, 2)



    if result == []:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {result[0]}')