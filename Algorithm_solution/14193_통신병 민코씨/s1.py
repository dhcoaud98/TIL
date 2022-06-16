import sys
sys.stdin = open('sampleinput.txt')


def f(y, x):
    pass


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(M)]
    print(arr)

    # 시작지점
