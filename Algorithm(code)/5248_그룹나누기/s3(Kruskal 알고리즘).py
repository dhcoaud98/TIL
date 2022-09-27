import sys
sys.stdin = open('sample_input.txt')


def findp(x):  # x의 루트를 찾음
    if parent[x] == x:
        return x
    else:
        return findp(parent[x])


def union(x, y):  # y의 루트의 부모는 x의 루트
    parent[findp(y)] = findp(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N+1)]

    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])
    result = []

    for j in parent:
        if findp(j) not in result:
            result.append(findp(j))
    print(f'#{tc} {len(result)-1}')
