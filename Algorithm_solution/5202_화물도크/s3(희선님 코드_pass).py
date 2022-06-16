import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr = sorted(arr, key=lambda x: (x[1]))  # 종료시점을 기준으로 정렬
    # arr = [[1, 4], [6, 15], [6, 15], [15, 16], [2, 19], [1, 22], [14, 23], [21, 23], [12, 24], [20, 24]]
    time = 0  # 0시부터 시작
    cnt = 0  # 화물차의 수
    for x, y in arr:
        if x >= time:  # 시작시간이 이전 작업 끝난 시점보다 크면
            time = y  # 시간을 종료시점으로 변경
            cnt += 1  # 화물차 + 1

    print(f'#{tc} {cnt}')
