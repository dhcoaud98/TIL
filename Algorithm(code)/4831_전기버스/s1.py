import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # K: 최대로 움직일 수 있는 수, N: 전체 정거장 수, M: 충전소가 있는 정거장 수
    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split()))
    # [1, 3, 5, 7, 9]
    # [1, 3, 7, 8, 9]
    # [4, 7, 9, 14, 17]

    # stop_station은 멈춘 정류장 수, now는 현재 위치
    stop_station = 0
    now = 0

    while now + K < N:

        for i in range(K, 0, -1):
            if (now + i) in charge_station:
                stop_station += 1
                now += i
                break
        # 충전소가 있는 곳에 멈추면 break문을 통해 while문으로 올라가고, for문을 다시 돌리게 되는데 이때, i값은 다시 3이다.
        # [4, 7, 9, 14, 17]
        else:
            stop_station = 0
            break

    print(f'#{tc} {stop_station}')




