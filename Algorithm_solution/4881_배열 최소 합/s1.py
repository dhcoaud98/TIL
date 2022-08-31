import sys
sys.stdin = open('sample_input.txt')

def dfs(r, lst, ssum):
    global result

    if ssum >= result:  # 가지치기
        return

    if r == N:
        if ssum <= result:
            result = ssum
    else:
        for i in range(N):
            if i not in visited:
                lst.append(i)
                dfs(r+1, lst, ssum+arr[r][i])
                lst.pop()


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = N*N*9
    visited = []
    dfs(0, visited, 0)
    print(f'#{tc} {result}')

