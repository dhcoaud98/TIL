import sys
sys.stdin = open('input.txt')


def DFS1(n):
    visited = [0]*(N+1)
    stack = []
    stack.append(n)
    visited[n] = 1
    # 1-2
    while stack:
        p = stack.pop()
        print(p, end=' ')
        for k in range(N+1):
            if visited[k] == 0 and arr[p][k] == 1:
                stack.append(k)
                visited[k] = 1

def DFS2(n):
    visited = [0]*(N+1)
    stack = []
    stack.append(n)
    visited[n] = 1
    # 1-3
    while stack:
        p = stack.pop()
        print(p, end=' ')
        for k in range(N, 0, -1):
            if visited[k] == 0 and arr[p][k] == 1:
                stack.append(k)
                visited[k] = 1


# main
lst = list(map(int, input().split(', ')))
# print(lst)
# 무뱡향 인접 행렬 만들기
N = 7
arr = [[0]*(N+1) for _ in range(N+1)]
# print(arr)
for i in range(0, len(lst), 2):
    arr[lst[i]][lst[i+1]] = 1
    arr[lst[i+1]][lst[i]] = 1
# print(arr)

DFS1(1)
print()
DFS2(1)