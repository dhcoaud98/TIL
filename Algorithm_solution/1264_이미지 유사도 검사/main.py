import sys
sys.stdin = open('input.txt')


def LCS():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if X_code[i-1] == Y_code[j-1]: # 두 문자가 같다면?
                lcs[i][j] = lcs[i-1][j-1] + 1
            elif X_code[i-1] != Y_code[j-1]:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    X_code = str(input())
    Y_code = str(input())
    answer = 0
    # print(X_code)
    # print(Y_code)

    lcs = [[0]*(N+1) for _ in range(N+1)]
    # print(lcs)
    LCS()
    answer = (lcs[N][N] / N) * 100
    print(f'#{tc} {format(answer,".2f")}')
