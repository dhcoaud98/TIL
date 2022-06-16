import sys
sys.stdin = open('input3.txt')

N = int(input())
arr = list(map(int, input().split()))

answer = []
max_up = 1
now = 0
while now < N-1:  # 오름차순
    if arr[now] <= arr[now+1]:
        max_up += 1
        now += 1
        if now == N-1:
            answer.append(max_up)
    else:
        answer.append(max_up)
        now += 1
        max_up = 1
if max_up == N:
    answer.append(max_up)

max_down = 1
now = 0
while now < N-1:  # 내림차순
    if arr[now] >= arr[now+1]:
        max_down += 1
        now += 1
        if now == N-1:
            answer.append(max_down)
    else:
        answer.append(max_down)
        now += 1
        max_down = 1

# print(answer)
print(max(answer))
