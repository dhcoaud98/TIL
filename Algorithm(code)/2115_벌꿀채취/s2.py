import sys
sys.stdin = open('sample_input.txt')



TC = int(input())
for tc in range(1, 2+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
