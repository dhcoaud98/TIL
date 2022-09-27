import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
temp = [[0]*5 for _ in range(5)]
number = []

for i in range(5):
    tell = list(map(int, input().split()))
    for t in tell:
        number.append(t)
print(number)
a = 0
answer = []
cnt = 0

for n in number:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                temp[i][j] += 1
                a += 1
                # 가로로 빙고가 나왓나?
                if sum(temp[i][:]) == 5:
                    cnt += 1
                # 세로로 빙고가 나왔나?
                elif sum(temp[:][j]) == 5:
                    cnt += 1
                # 대각선으로 빙고가 나왔나?
                if temp[0][0] + temp[1][1] + temp[2][2] + temp[3][3] + temp[4][4] == 5:
                    cnt += 1
                elif temp[0][4] + temp[1][3] + temp[2][2] + temp[3][1] + temp[4][0] == 5:
                    cnt += 1
                # 빙고가 세개면 종료!
                if cnt == 3:
                    answer.append(a)

print(answer[0])