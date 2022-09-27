import sys

sys.stdin = open('sample_input.txt')

TC = int(input())  # 3

for tc in range(1, TC+1):
    # 1
    # 조건과 예시
    # [10, 3] - cond[0]은 10개의 정수, cond[1]은 이웃한 3개
    # ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cond = list(map(int, input().split()))
    ex = list(map(int, input().split()))

    # 2
    # 이웃한 3개의 리스트로 다시 묶기
    # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]
    ans_list = []
    for i in range(0, cond[0] - cond[1] + 1):  # range(0, 10-3+1)
        ans_list.append(ex[i:i+cond[1]])

    # 3
    # 리스트 합 구하기
    # [6, 9, 12, 15, 18, 21, 24, 27]
    ans_list_1 = []
    for ans in ans_list:
        my_sum = 0
        for i in range(0, cond[1]):
            my_sum += ans[i]
        ans_list_1.append(my_sum)

    # 4
    # ans_list_1에서 가장 큰 수와 가장 작은 수 차이 구하기
    max_num = ans_list_1[0]
    min_num = ans_list_1[0]
    for i in range(0, len(ans_list_1)):
        if ans_list_1[i] >= max_num:
            max_num = ans_list_1[i]
        if ans_list_1[i] <= min_num:
            min_num = ans_list_1[i]

    result = max_num - min_num

    print(f'#{tc} {result}')