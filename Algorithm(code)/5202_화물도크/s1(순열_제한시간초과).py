import sys
sys.stdin = open('sample_input.txt')
# 시간 초과로 통과x

def pick(idx, n):
    global result, hours, overlap_time, a
    if idx == -1:
        # print(bits)
        if sum(bits) > result:
            hours = [0] * 24
            for i in range(len(bits)):
                if bits[i] == 1:
                    for j in range(arr[i][0], arr[i][1]):
                        hours[j] += 1

            overlap_time = 0
            for i in range(len(hours)):
                if hours[i] >= 2:
                    break
                if i == 23:
                    if result <= sum(bits):
                        result = sum(bits)
    else:
        bits[idx] = 1
        pick(idx-1, n)
        bits[idx] = 0
        pick(idx-1, n)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0과 1로 이루어진 부분집합 구하기
    result = 0
    overlap_time = 0
    hours = [0] * 24
    bits = [0] * N

    pick(N-1, 0)

    print(f'#{tc} {result}')
