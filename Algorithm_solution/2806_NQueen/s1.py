import sys
sys.stdin = open('sample_input.txt')


def DFS(n):
    global result
    if n == N:  # 마지막 행까지 도달했다면 result를 +1 해줌
        result += 1
        return
    else:
        for i in range(N):
            if visited[i] == 1:  # 방문한 곳이면 pass
                continue

            board[n] = i  # (n, i)에 퀸 올리기
            print(board)
            if check(n):  # n행에 퀸을 올릴 수 있는지?
                visited[i] = True
                DFS(n+1)
                visited[i] = False
def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (n-i == abs(board[n]-board[i])):
            return False

    return True


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    result = 0
    board = [[0] * N for _ in range(N)]
    visited = [False] * (N + 1)

    DFS(0)


    print(f'#{tc} {result}')