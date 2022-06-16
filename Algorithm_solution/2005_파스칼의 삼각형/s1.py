import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    print(f'#{tc}')
    temp = []
    for i in range(N):
        for j in range(i+1):
            # 첫인덱스와 마지막인덱스는 1
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(temp[-i]+temp[-i-1])

    now = 0
    for i in range(1, N+1):
        print(*temp[now:now+i])
        now += i

