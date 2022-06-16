import sys
sys.stdin = open('input.txt')

S = int(input())
swith = [0] + list(map(int, input().split()))
# [0, 0, 1, 0, 1, 0, 0, 0, 1]
P = int(input())
for i in range(P):
    W_M, number = map(int, input().split())

    # 계산
    if W_M == 1:  # 남자
        for j in range(1, S//number+1):
            if swith[number*j] == 1:
                swith[number*j] = 0
            else:
                swith[number*j] = 1
    # [0, 0, 1, 1, 1, 0, 1, 0, 1]
    elif W_M == 2:  # 여자
        # number자리의 스위치를 1<->0
        if swith[number] == 1:
            swith[number] = 0
        else:
            swith[number] = 1

        # 범위 구하기
        if (number - 1) <= (S - number):
            min_range = number - 1
        else:
            min_range = S - number

        # 스위치 변경
        for k in range(1, min_range+1):
            if swith[number-k] == swith[number+k] == 1:
                swith[number - k] = 0
                swith[number + k] = 0
            elif swith[number-k] == swith[number+k] == 0:
                swith[number - k] = 1
                swith[number + k] = 1
            else:
                break


for m in range(1, len(swith), 20):
    print(*swith[m:m+20])

