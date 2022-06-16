import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

students = [[0] * 2 for _ in range(7)]

for n in range(N):
    S, C = map(int, input().split())
    students[C][S] += 1
print(students)

rooms = 0
for i in range(1, 7):
    for j in range(0, 2):
        if 0 < students[i][j] <= K:
            rooms += 1
        elif students[i][j] > K:
            if students[i][j] % K == 0:
                rooms += (students[i][j] / K)
            else:
                rooms += (students[i][j] // K + 1)

print(int(rooms))
