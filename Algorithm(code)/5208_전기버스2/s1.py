import sys
sys.stdin = open('sample_input.txt')


def f(idx, s):  # 인덱스, battery
    global result
    if result < s:  # 가지치기
        return
    if idx >= arr[0]:
        result = s-1  # idx = 2에서 출발하는 것은 횟수에 넣어주지 않기 때문
        return
    cnt = arr[idx]  # 가장 멀리 갈 수 있는 값 찾기
    for i in range(cnt, 0, -1):
        f(idx+i, s+1)


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    result = len(arr)
    f(1, 0)

    print(f'#{tc} {result}')
