import sys

sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')


def Basic(P, T):
    cnt = 0

    for i in range(T_len):
        if T[i:i+P_len] == P[:]:
            cnt += 1

    return f'#{now} {cnt}'




for tc in range(1, 11):
    # now는 테스트 케이스 번호, P는 패턴, T는 테이블, P_len은 P길이, N_len은 T길이
    now = input()
    P = input()
    T = input()
    P_len = len(P)
    T_len = len(T)

    print(Basic(P, T))