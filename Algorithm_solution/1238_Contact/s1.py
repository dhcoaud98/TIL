import sys
sys.stdin =open('input.txt')


def my_call(graph, s):
    visited = [0]*101
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        q = queue.pop(0)
        if visited[s] < visited[q] or visited[s] == visited[q] and s < q:
            s = q
        for k in range(1, 101):
            if matrix[q][k] == 1 and visited[k] == 0:
                queue.append(k)
                # 단계가 달라지면 1 더하기!!
                visited[k] = visited[q] + 1

    return s

for tc in range(1, 11):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))
    matrix = [[0]*101 for _ in range(101)]

    # 이차원 배열을 만들었다. 인접행렬 만들기
    for i in range(0, N, 2):
        matrix[lst[i]][lst[i+1]] = 1

    # 이차원 배열의 가로로 움직임!!
    print(f'#{tc}', end= ' ')
    print(my_call(matrix, start))

