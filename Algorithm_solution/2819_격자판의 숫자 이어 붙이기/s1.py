import sys
sys.stdin =open('sample_input.txt')

def number(y, x, cnt, lst):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    if cnt == 7:
        # print(lst)
        if lst not in result:
            result.append(lst)

    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 4 and 0 <= ny < 4:
                lst += arr[ny][nx]
                number(ny, nx, cnt+1, lst)
                lst = lst[:-1]  # str은 인덱스로 제거할 수 없으므로 슬라이싱을 이용했다.


TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    result = []
    for i in range(4):
        for j in range(4):
            lst = ''
            number(i, j, 0, lst)

    print(f'#{tc} {len(result)}')