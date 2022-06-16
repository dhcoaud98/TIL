import sys

sys.stdin = open('s_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # 1. 테스트 케이스 조건
    bus_noseon_cnt = int(input())
    bus_noseon = [list(map(int, input().split())) for _ in range(bus_noseon_cnt)]
    bus_station_cnt = int(input())
    bus_station = [int(input()) for _ in range(bus_station_cnt)]


    # 2. 계산
    temp = [0] * 5001  # 모든 정류소를 0으로 초기화
    for i in range(bus_noseon_cnt):
        K = bus_noseon[i][1] - bus_noseon[i][0]
        for m in range(K+1):
            temp[bus_noseon[i][0]+m] += 1


    # 3. 출력
    result = ''
    for i in range(bus_station_cnt):
        result += ' ' + str(temp[bus_station[i]])

    print(f'#{tc}{result}')





