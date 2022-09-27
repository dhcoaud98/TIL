import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, 2+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로로 한줄 씩 탐방하기
    # 1. 한 줄의 값이 모두 같다면 reault + 1
