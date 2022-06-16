import sys
sys.stdin = open('input.txt')

temp = [[0] * 101 for _ in range(101)]
TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())

    for m in range(M, M+10):
        for n in range(N, N+10):
            temp[m][n] += 1

cnt = 0
for i in range(len(temp)):
    for j in range(len(temp)):
        if temp[i][j] >= 1:
            cnt += 1

# print(temp)
print(cnt)
