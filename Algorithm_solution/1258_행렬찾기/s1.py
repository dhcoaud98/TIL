import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(arr)
    sub_matrix = 0
    col_list = []
    row_list = []
    for i in range(N):
        col = row = now = 0
        for j in range(N):
            if arr[i+now][j] != 0:
                col += 1
            else:
                for k in range(N):
                    if arr[i+now][j-1] != 0:
                        row += 1
                        now += 1
                    else:
                        break

        col_list.append(col)
        row_list.append(row)
    print(row_list, col_list)






    # if N <= 10:
    #
    # elif N < 40:
    #     pass
    # elif 40 < N <= 80:
    #     pass
    # elif 80 < N <=100:
