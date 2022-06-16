import sys
sys.stdin = open('input.txt')

N = int(input())
Students = list(map(int, input().split()))

temp = [0] * N
temp[0] = 1

for i in range(1, N):
    for j in range(i-1, i-1-Students[i], -1):
        temp[j+1] = temp[j]
    temp[i-Students[i]] = i+1

print(*temp)


