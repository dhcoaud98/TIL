import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, 2+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로
    for i in range(N):
        cnt = 0
        max_idx = []
        max_num = max(arr[i])
        for j in range(N):
            if arr[i][j] == max_num:
                cnt += 1
                max_idx.append(j)
                         
        if cnt == N:  # 한 줄의 값이 모두같으면
            result += 1

        # print(max_idx)
        l, h = [], []
        l = arr[i][:max_idx[0]:-1]
        h = arr[i][max_idx[-1]+1:]
        print(l, h)

        temp = []
        max_num = max(arr[i])-1
        up = 0
        if len(h) == 0:
            up = 1
        else:
            for j in range(len(h)):
                if h[0] == max_num:
                    p = h.pop(0)
                    temp.append(p)
                else:
                    if len(temp) >= X:
                        max_num -= 1
                        temp = []
                        temp.append(h.pop(0))
                    else:
                        break

        if len(temp) >= X:
            up = 1

        temp = []
        max_num = max(arr[i])-1
        down = 0
        if len(l) == 0:
            down = 1
        else:
            for j in range(len(l)):
                if l[0] == max_num:
                    p = l.pop(0)
                    temp.append(p)
                else:
                    if len(temp) >= X:
                        max_num -= 1
                        temp = []
                        temp.append(l.pop(0))
                    else:
                        break

        if len(temp) >= X:
            down = 1

    if up == 1 and down == 1:
        result += 1

    print(f'#{tc} {result}')
