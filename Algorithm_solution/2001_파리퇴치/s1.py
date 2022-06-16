import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # 전체 N*N 행렬과 파리채 M*M 행렬
    N, M = map(int, input().split())

    # N*N 행렬을 target_list로 만들어주기
    # tc = 1 / [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]
    target_list = []
    for n in range(0, N):
        target_list.append(list(map(int, input().split())))

    # N*N 행렬 중 M*M 행렬을 뽑아내 합한 값을 catchs에 넣기
    # tc=1 / [25, 28, 30, 33, 41, 49, 44, 38, 26, 32, 47, 43, 28, 22, 35, 35]
    catchs = []
    my_sum = 0
    now1 = 0
    now2 = 0

    while now2 < N - M + 1:
        my_sum = 0

        if now1 < N - M + 1:
            for i in range(0, M):
                for j in range(0, M):
                    my_sum += target_list[i+now2][j+now1]
            now1 += 1
            catchs.append(my_sum)
        else:
            now1 = 0
            now2 += 1

    # 최댓값 구하기
    max_num = catchs[0]
    for catch in catchs:
        if catch >= max_num:
            max_num = catch

    print(f'#{tc} {max_num}')



    