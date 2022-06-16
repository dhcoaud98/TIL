import sys
sys.stdin = open('sample_sample_input.txt')


def sol(cnt, ssum, lst, operate_lst):
    global answer
    """
    :param cnt: 현재 연산 횟수
    :param ssum: 현재 연산된 계산값
    :param lst: 가능한 숫자 list
    :param operate_lst: 가능한 연산자 list
    :return: ssum
    """
    if cnt > int(M):  # 연산 횟수가 넘어가면 가지치기
        return

    if ssum == result:  # 결과 값이 나왔다면?
        if cnt <= answer:
            answer = cnt
            return






TC = int(input())
for tc in range(1, TC+1):
    N, O, M = input().split()
    possible = list(map(int, input().split()))
    possible_operate = list(map(int, input().split()))
    result = int(input())
    answer = 20

    if result < 10 and result in possible:
        print(f'#{tc} {1}')

    elif result >= 10:  # 연산자가 필요하지 않은 경우
        temp = []
        a = 0
        while result > 10:
            temp.append(result % 10)
            result = result // 10
        temp.append(result)

        for i in range(len(temp)):
            if temp[i] in possible:
                a += 1
        if a == len(temp):
            print(f'#{tc} {a}')
        else:
            sol(0, 0, possible, possible_operate)
            print(f'#{tc} {answer}')


