import sys
sys.stdin = open('input.txt')

temp = [[0] * 101 for _ in range(101)]
cnt = 0
for i in range(4):
    xa, ya, xb, yb = map(int, input().split())
    for m in range(xa, xb):
        for n in range(ya, yb):
            temp[m][n] += 1

for i in range(101):
    for j in range(101):
        if temp[i][j] >= 1:
            cnt += 1

print(cnt)

