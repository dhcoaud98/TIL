import sys
sys.stdin = open('input2.txt')

K = int(input())

# D = 1, 2는 가로 D = 3, 4는 세로
max_width = 0
max_height = 0
max_width_idx = 0
max_height_idx = 0

D_L = [list(map(int, input().split())) for _ in range(6)]
# [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]
# print(D_L)

# 가로, 세로 최댓값 인덱스 구하기
for i in range(6):
    if D_L[i][0] == 1 or D_L[i][0] == 2:
        if D_L[i][1] >= max_width:
            max_width = D_L[i][1]
            max_width_idx = i
    else:
        if D_L[i][1] >= max_height:
            max_height = D_L[i][1]
            max_height_idx = i
# print(max_width, max_width_idx, max_height, max_height_idx)

# 최대 사각형과 최소 사각형
biggest = max_width * max_height

min_heigth = abs(D_L[(max_width_idx + 5) % 6][1] - D_L[(max_width_idx+1) % 6][1])
min_width = abs(D_L[(max_height_idx + 5) % 6][1] - D_L[(max_height_idx+1) % 6][1])
smallest = min_width * min_heigth

area = biggest - smallest

print(area*K)


