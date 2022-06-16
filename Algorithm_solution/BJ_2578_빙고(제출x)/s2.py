import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
print(arr)
temp = [[0]*5 for _ in range(5)]
number = []

for i in range(5):
    tell = list(map(int, input().split()))
    for t in tell:
        number.append(t)
print(number)
stop = 0
answer = []
for n in number:
    cnt = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0
                stop += 1
                # 가로에 빙고?
                for k in range(5):
                    if sum(arr[k][:]) == 0:
                        cnt += 1
                        if cnt == 3:
                            answer.append(stop)
                            # print(stop)
                            break
                # 세로에 빙고?
                for k in range(5):
                    if sum(arr[:][k]) == 0:
                        cnt += 1
                        if cnt == 3:
                            answer.append(stop)
                            # print(stop)
                            break
                # 대각선에 빙고?
                if arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] == 0:
                    cnt += 1
                    if cnt == 3:
                        answer.append(stop)
                        # print(stop)
                        break
                if arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0] == 0:
                    cnt += 1
                    if cnt == 3:
                        answer.append(stop)
                        # print(stop)
                        break

print(answer[0])