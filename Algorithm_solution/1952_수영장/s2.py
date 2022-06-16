import sys
sys.stdin = open('sample_input.txt')


def DFS(n, pay):
    global result

    if n >= 13:
        if result >= pay:  # 종료 조건
            result = pay
        return
    else:
        # 1년
        DFS(n+12, pay+pays[3])
        # 3개월
        DFS(n+3, pay+pays[2])
        # 1개월
        DFS(n+1, pay+pays[1])
        # 1일권
        DFS(n+1, pay+pays[0]*calendar[n])


TC = int(input())
for tc in range(1, TC+1):
    pays = list(map(int, input().split()))
    calendar = [0]+list(map(int, input().split()))
    result = 12345678
    DFS(1, 0)
    print(f'#{tc} {result}')