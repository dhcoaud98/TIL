import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    temp = [0] * (N+1)
    number = list(map(int, input().split()))
    # number = [7, 2, 5, 3, 4, 6]
    # temp = [0, 7, 0, 0 , 0, 0, 0]
    temp[1] = number[0]

    for i in range(2, N+1):
        temp[i] = number[i-1]
        k = i
        while k > 1:  # 부모 노드가 자식 노드 보다 작아야 하기 때문에 루트까지 비교를 계속 반복한다.
            if temp[k//2] > temp[k]:
                temp[k//2], temp[k] = temp[k], temp[k//2]
            k = k//2
    # print(temp)

    result = 0
    while N > 1:
        result += temp[N//2]
        N = N//2

    print(f'#{tc} {result}')
