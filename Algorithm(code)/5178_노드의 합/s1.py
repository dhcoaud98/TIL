import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M, L = map(int, input().split())

    temp = [0] * (N+1)
    for i in range(M):
        A, B = map(int, input().split())
        temp[A] = B
    # print(temp)
    # print(L)
    end = N
    # temp[L] = temp[L * 2] + temp[L * 2 + 1]
    # 이진트리의 왼쪽값은 짝수임을 이용한다.
    while end > L+1:
        if end % 2 == 0:  # 마지막이 짝수
            if temp[end//2] == 0 and end == N:  # 제일 마지막이면 1개밖에 없으므로
                temp[end//2] = temp[end]
            elif temp[end//2] == 0:  # 그 다음부터는 두개씩 더하기
                temp[end//2] = temp[end] + temp[end+1]
            end -= 2
        else:  # 마지막이 홀수
            if temp[end//2] == 0:  # 두개씩 더하기
                temp[end//2] = temp[end] + temp[end-1]
            end -= 2

    print(f'#{tc} {temp[L]}')