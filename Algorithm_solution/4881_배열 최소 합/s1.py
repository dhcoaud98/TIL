import sys
sys.stdin = open('sample_input.txt')

def adjacent(x):  # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
    for i in range(x):  # 인덱스가 행  row[n]값이 열
        if row[x] == row[i]:  # 열이 같으면 false
            return False
    return True


# 한줄씩 재귀하며 dfs 실행
def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):  # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            row[x] = i
            if adjacent(x):  # 행,열 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x + 1)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row = [0] * N
    result = 0
    print(row)
    dfs(0)
    # print(row)
    print(result)


