import sys
sys.stdin = open('input.txt')

N = int(input())
Length = []
Heigth = []

for n in range(N):
    L, H = map(int, input().split())
    Length.append(L)
    Heigth.append(H)
# [2, 11, 15, 4, 5, 8, 13] [4, 4, 8, 6, 3, 10, 6]
# print(Length, Heigth)

# 1. 그래프 그리기
K = max(Length)
temp = [0] * (K+1)
for i in range(len(Length)):
    temp[Length[i]] = Heigth[i]
# print(temp)


# 2. 최댓값의 인덱스 구하기
for i in range(len(Length)):
    if Heigth[i] == max(Heigth):
        max_idx = Length[i]
# print(max_idx)

# 3. 최댓값까지는더하고, 그 다음부터는 역으로 움직임.
for i in range(1, max_idx+1):
    if temp[i] <= temp[i-1]:
        temp[i] = temp[i-1]
# print(temp)
for i in range(K, max_idx+1, -1):
    if temp[i-1] <= temp[i]:
        temp[i-1] = temp[i]
# print(temp)
print(sum(temp))








