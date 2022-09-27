import sys

sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')


def BruteForce(P, T):
    i = 0  # p의 인덱스  # ti
    j = 0  # t의 인덱스  # Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition
    cnt = 0

    while j < T_len:

        if T[j] == P[i]:
            i = i + 1
            j = j + 1
        elif T[j] != P[i]:
            i = 0
            j += 1
            if j == 0 and i == 0:
                j = 1
                i = 0

        if i == P_len:
            cnt += 1
            i = 0

    return cnt




for tc in range(1, 11):
    # now는 테스트 케이스 번호, P는 패턴, T는 테이블, P_len은 P길이, N_len은 T길이
    now = input()
    P = input()
    T = input()
    P_len = len(P)
    T_len = len(T)

    print(BruteForce(P, T))