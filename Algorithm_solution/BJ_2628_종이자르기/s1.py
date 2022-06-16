import sys
sys.stdin = open('input.txt')

W, H = map(int, input().split())
temp = [[0] * (W+1) for _ in range(H+1)]

# 1로 cut하기
# 자름 선이 있는 지점
# [0, 4, 10] [0, 2, 3, 8]
Cut = int(input())
width_list = [0]
height_list = [0]
for i in range(Cut):  # 0은 가로, 1은 세로
    N, M = map(int, input().split())
    if N == 0:
        height_list.append(M)
    else:
        width_list.append(M)

width_list.sort()
height_list.sort()
width_list.append(W)
height_list.append(H)

# 가로의 최댓값, 세로의 최댓값
a = []
b = []
for i in range(len(width_list)-1, 0, -1):
    a.append(width_list[i]-width_list[i-1])

for i in range(len(height_list)-1, 0, -1):
    b.append(height_list[i]-height_list[i-1])

area = max(a)*max(b)
print(area)
