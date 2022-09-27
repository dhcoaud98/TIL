import sys
sys.stdin = open('input')


def BFS(n):
    visited = [0]*(V+1)
    queue = []
    queue.append(n)
    visited[n] = 1
    while queue:
        q = queue.pop(0)
        print(q, end=' ')
        for k in range(1, 8):
            if arr[q][k] == 1 and visited[k] == 0:
                visited[k] = 1
                queue.append(k)

lst = list(map(int, input().split(', ')))
V = 7
arr = [[0]*(V+1) for _ in range(V+1)]
# print(arr)
for i in range(0, len(lst), 2):
    arr[lst[i]][lst[i+1]] = 1
    arr[lst[i+1]][lst[i]] = 1
# print(arr)

BFS(1)