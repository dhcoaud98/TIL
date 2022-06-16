import sys
sys.stdin = open('sample_in.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    temp = [0] * 1001
    for n in range(N):
        P, A, B = map(int, input().split())

        if P == 1:  # 일반버스
            for i in range(A, B+1):
                temp[i] += 1
        elif P == 2:  # 급행버스
            if A % 2 == 0:  # A가 짝수이면
                for i in range(A, B+1, 2):
                    temp[i] += 1
            else:  # A가 홀수이면
                for i in range(A, B+1, 2):
                    temp[i] += 1
        else:  # 광역버스
            if A % 2 == 0:  # A가 짝수이면
                for i in range(A, B+1):
                    if i % 4 == 0:
                        temp[i] += 1
            else:  # A가 홀수이면
                for i in range(A, B+1):
                    if i % 3 == 0 and i % 10 != 0:
                        temp[i] += 1

    print(f'#{tc} {max(temp)}')