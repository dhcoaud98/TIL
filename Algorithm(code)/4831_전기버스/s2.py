import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

for p in range(tc):
    numbs = list(map(int, input().split()))
    k = numbs[0]
    n = numbs[1]
    m = numbs[2]
    stops = list(map(int, input().split()))

    supply_stop = [0] * (n+1)
    for q in range(m):
        supply_stop[stops[q]] = 1 # 표 생성, 충전소 지점에 1

    pos = 0
    cnt = 0
    temp = []

    while(pos < n):
        temp = []
        if (pos + k) >= n:
            break

        for q in range(k):
            if supply_stop[pos + q + 1] == 1:
                temp.append(pos + q + 1)
        if temp == []:
            cnt = 0
            break

        pos = temp[-1]
        cnt += 1

    print(f'#{p+1} {cnt}')