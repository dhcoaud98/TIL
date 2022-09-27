import sys

sys.stdin = open('sample_input.txt')

# 테스트 케이스와 각 테스트 게이스별 양수의 갯수
TC = list(map(int, input().split()))


for tc in range(1, TC[0]+1):
    cnt = list(map(int, input().split()))
    ans_list = list(map(int, input().split()))
    # max_min의 index 0 은 최댓값을 index 1 은 최솟값을 표현하기로 함.
    max_min = [ans_list[0], ans_list[0]]

    for c in range(0, cnt[0]):
        if ans_list[c] >= max_min[0]:
            max_min[0] = ans_list[c]

        if ans_list[c] <= max_min[1]:
            max_min[1] = ans_list[c]



    result = max_min[0] -max_min[1]
    print(f'#{tc} {result}')
