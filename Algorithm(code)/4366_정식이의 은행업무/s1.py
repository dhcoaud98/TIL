import sys
import copy
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    binary = list(map(int, input()))
    third = list(map(int, input()))

    # 잘못된 이진코드 읽기
    A = []
    for i in range(len(binary)):
        bin_to_dec = 0
        result = copy.deepcopy(binary)
        if result[i] == 1:
            result[i] = 0
        else:
            result[i] = 1
        result = result[::-1]

        for k in range(len(result)):
            bin_to_dec += (2**k)*result[k]
        A.append(bin_to_dec)

    # 잘못된 삼진코드 읽기
    B = []
    result = copy.deepcopy(third)
    for i in range(len(third)):
        if result[i] == 2:
            for j in range(0, 2):
                thi_to_dec = 0
                result = copy.deepcopy(third)
                result = result[::-1]
                result[i] = j
                for k in range(len(result)):
                    thi_to_dec += (3**k)*result[k]
                B.append(thi_to_dec)
        elif result[i] == 1:
            for j in range(0, 3, 2):
                thi_to_dec = 0
                result = copy.deepcopy(third)
                result = result[::-1]
                result[i] = j
                for k in range(len(result)):
                    thi_to_dec += (3 ** k) * result[k]
                B.append(thi_to_dec)
        else:
            for j in range(1, 3):
                thi_to_dec = 0
                result = copy.deepcopy(third)
                result = result[::-1]
                result[i] = j
                for k in range(len(result)):
                    thi_to_dec += (3 ** k) * result[k]
                B.append(thi_to_dec)


    print(f'#{tc} ', end='')
    for i in range(len(binary)):
        if A[i] in B:
            print(A[i], end='')