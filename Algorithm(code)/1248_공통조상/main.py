import sys
sys.stdin = open('input.txt')


def sol(a, b):
    global answer, cnt, result, total

    queue = [a]
    while queue:
        p = queue.pop(0)
        for i in range(1, V+1):
            if matrix[p][i] == 1:
                parentA.append(i)
                queue.append(i)

    queue = [b]
    while queue:
        p = queue.pop(0)
        for j in range(1, V+1):
            if matrix[p][j] == 1:
                if j in parentA:
                    total = j
                    break
                parentB.append(j)
                queue.append(j)

    # answer의 서브 트리 크기 구하기
    queue = [total]
    while queue:
        p = queue.pop(0)
        for c in range(len(child[p])):
            queue.append(child[p][c])
            cnt += 1


TC = int(input())
for tc in range(1, TC+1):
    V, E, A, B = map(int, input().split())

    arr = list(map(int, input().split()))


    matrix = [[0]*(V+1) for _ in range(V+1)]
    # print(matrix)
    answer = 1
    cnt = 1
    result = []
    for i in range(0, 2*E, 2):
        matrix[arr[i+1]][arr[i]] = 1

    total = 0

    child = [[] for _ in range(V+1)]
    # print(child)
    for i in range(0, 2*E, 2):
        child[arr[i]].append(arr[i+1])
    # print(child)


    parentA, parentB = [], []
    # print(matrix)
    sol(A, B)

    print(f'#{tc} {total} {cnt}')
