import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 기법 사용 예정!
def DFS(n, alst, blst):
    global ans
    if n == N:  # 유먕한지 유망하지 않은지?
        if len(alst) == len(blst):  # 유먕한지 유망하지 않은지?
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(blst)):
                    asum += score[alst[i]][alst[j]]
                    bsum += score[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)

        return
    DFS(n+1, alst+[n], blst)
    DFS(n+1, alst, blst+[n])



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    ans = 123456
    DFS(0, [], [])
    print(f'#{tc} {ans}')
