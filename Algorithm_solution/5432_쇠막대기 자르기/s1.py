import sys


sys.stdin = open('sample_input.txt')


TC = int(input())
for tc in range(1, TC+1):
    cont = input()
    L = len(cont)
    # ()(((()())(())()))(())
    # !! 레이저 끝나면 앞의 sol에 cnt 값을 더함, 만약 막대기가 끝나면 sol에 1을 더함
    cnt = 0
    sol = 0
    for i in range(L):
        if cont[i] == '(':  # 막대기 추가
            cnt += 1
        else:
            if cont[i-1] == '(':  # 레이저
                cnt -= 1
                sol += cnt
            else:  # 막대기 제거
                cnt -= 1
                sol += 1

    print(f'#{tc} {sol}')







