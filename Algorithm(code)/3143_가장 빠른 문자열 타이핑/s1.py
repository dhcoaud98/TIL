import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # T는 테이블, P는 패턴
    T, P = input().split()

    # 1. T에서 P가 몇개 나오는지 세기
    cnt = 0
    result = 0
    now = 0
    # for i in range(len(T)-len(P)+1):
    while now < len(T)-len(P)+1:
        if T[now:now+len(P)] == P[:]:
            now += len(P)
            cnt += 1
        else:
            now += 1

    # 2. 값 계산
    # result = (반복문 빼고 나머지 개수) + (반복문 개수)
    result = (len(T)-cnt*len(P)) + cnt

    print(f'#{tc} {result}')