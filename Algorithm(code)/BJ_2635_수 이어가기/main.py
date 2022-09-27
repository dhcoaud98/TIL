import sys
sys.stdin = open('input.txt')

num = int(input())
answer = []
max_len = 0

# num에 따른 규칙 구하기
for i in range(1, num+1):
    temp = []
    temp.append(num)
    temp.append(i)
    while temp[-2] - temp[-1] > -1:
        temp.append(temp[-2] - temp[-1])
    answer.append(temp)
    
# 길이 최댓값 구하기
for i in range(len(answer)):
    if len(answer[i]) > max_len:
        max_len = len(answer[i])

# 길이가 최댓값과 같을 때 그 길이와 값 출력 
for i in range(len(answer)):
    if len(answer[i]) == max_len:
        print(max_len)
        print(*answer[i])
        break





