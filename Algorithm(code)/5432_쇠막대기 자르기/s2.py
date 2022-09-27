import sys


sys.stdin = open('sample_input.txt')


TC = int(input())
for tc in range(1, TC+1):
    P = input()
    L = len(P)

    # (가 나오면 +1 )가 나오면 -1
    cnt = result = 0
    for i in range(L):
        # ()(((()())(())()))(())
        if P[i] == '(':
            cnt += 1
        else:  # P[i] == ')'
            if P[i-1] == '(':  # 레이저
                cnt -= 1
                result += cnt
            else:
                cnt -= 1
                result += 1

    print(result)



