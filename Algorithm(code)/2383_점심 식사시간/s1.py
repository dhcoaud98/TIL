import sys
sys.stdin = open('sample_input.txt')

"""
1. 계단 1과 계단 2에 내려갈 수 있는 사람을 먼저 부분집합으로 구해주기
2. 계단까지 움직이기 위한 거리 구하기
    이때, 움직이는 거리 오름차순으로 정렬하기(가장 작은 값일 수록 가장먼저 도착하므로)
3. 계단 1과 계단 2에 내려갈 수 있는 마지막 사람과 인덱스 [-4]인 사람과 비교해 계단1, 계단2에서 오래걸리는 값 찾기
4. 찾은 값에서 작은 값 출력
"""


def people_to_stair(idx):
    """
    :param idx: 인덱스
    :return: 계단 1과 2에 사람 나누기
    """
    stair1 = []
    stair2 = []
    if idx == len(people):
        # print(bit)
        for b in range(len(bit)):
            if bit[b] == 0:
                stair1.append(people[b])
            else:
                stair2.append(people[b])
        move_time(0, stair1, stair2)
        return
    else:
        bit[idx] = 0
        people_to_stair(idx+1)
        bit[idx] = 1
        people_to_stair(idx+1)


def move_time(n, stair1, stair2):
    """
    :param n: 현재 시간
    :param stair1: 첫 번째 계단 리스트
    :param stair2: 두 번째 계단 리스트
    :return: n
    """
    global stair
    stair1_time = [0] * len(stair1)
    stair2_time = [0] * len(stair2)

    for k in range(len(stair1)):
        stair1_time[k] = abs(stair1[k][0] - stair[0][0]) + abs(stair1[k][1] - stair[0][1])
    for k in range(len(stair2)):
        stair2_time[k] = abs(stair2[k][0] - stair[1][0]) + abs(stair2[k][1] - stair[1][1])

    stair1_time.sort()
    stair2_time.sort()
    move1(stair1_time)
    move2(stair2_time)

    if result1 >= result2:
        answer.append(result1)
    else:
        answer.append(result2)

    return answer


def move1(stair1_time):  # 첫번째 계단에 온 사람들 전부 내려가는데 걸리는 시간 구하기
    global result1

    if len(stair1_time) >= 4:
        if stair1_time[-1] >= stair1_time[-4] + stair_time[0] + 1:
            result1 = stair1_time[-1] + stair_time[0] + 1
        else:
            result1 = stair1_time[-4] + 2*stair_time[0] + 1
    elif len(stair1_time) == 0:
        result1 = 0
    elif 0 < len(stair1_time) < 4:
        result1 = stair1_time[-1] + stair_time[0] + 1

    return result1


def move2(stair2_time):  # 두번째 계단에 온 사람들 전부 내려가는데 걸리는 시간 구하기
    global result2

    if len(stair2_time) >= 4:
        if stair2_time[-1] >= stair2_time[-4] + stair_time[1] + 1:
            result2 = stair2_time[-1] + stair_time[1] + 1
        else:
            result2 = stair2_time[-4] + 2*stair_time[1] + 1
    elif len(stair2_time) == 0:
        result2 = 0
    elif 0 < len(stair2_time) < 4:
        result2 = stair2_time[-1] + stair_time[1] + 1

    return result2


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
    result1 = result2 = 0
    answer = []

    # 1. 사람의 위치 찾기
    people = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                people.append([i, j])

    # 2. 계단의 위치 찾기
    stair = []
    stair_time = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] >= 2:
                stair.append([i, j])
                stair_time.append(arr[i][j])

    # 3. 계단 두개에 사람 나누어 넣기. 이때 계단에 한 사람도 안내려 갈 수도 있다.
    bit = [0]*len(people)
    people_to_stair(0)
    print(f'#{tc} {min(answer)}')
