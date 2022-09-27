import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    table = ['0001101', '0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    pattern = []
    idx = -1

    # 1.뒤에서부터 탐색하여 배열 안에서 코드 찾아내기
    for i in range(N):
        idx = -1
        while abs(idx) < M-1:  # 뒤에서부터 탐색
            if arr[i][idx] == '1':
                pattern.append(arr[i][idx-6:idx+1])
                idx -= 7
            else:
                idx -= 1
    pattern = pattern[0:8]
    # [['0', '1', '1', '1', '0', '1', '1'], ['0', '0', '1', '0', '0', '1', '1'], ['0', '0', '0', '1', '1', '0', '1'], ...


    # 2. 찾아낸 코드 뒤에서부터 순차적으로 탐색 하여 주어진 table안에 값이 있는지?
    my_sum = []
    for i in range(7, -1, -1):
        new = 0
        new = ''.join(pattern[i])
        for j in range(10):
            if new == table[j]:
                my_sum.append(int(j))
    # [7, 5, 7, 5, 5, 0, 2, 7]

    # 3. 올바른 코드인지?
    result = (my_sum[0] + my_sum[2] +my_sum[4] +my_sum[6])*3 + my_sum[1] +my_sum[3] + my_sum[5] +my_sum[7]
    if result % 10 == 0:
        print(f'#{tc} {sum(my_sum)}')
    else:
        print(f'#{tc} 0')
