import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # 전체 쪽 수, A가 찾을 쪽 수, B가 찾을 쪽 수
    P, A, B = map(int, input().split())
    arr = [i for i in range(0, P)]
    # print(P, A, B, arr)

    # A
    start = 1  # 0
    end = P  # 400
    cntA = 0
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == A:
            cntA += 1
            break
        elif arr[middle] > A:
            end = middle
            cntA += 1
        else:
            start = middle
            cntA += 1
    # B
    start = 1
    end = P
    cntB = 0
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == B:
            cntB += 1
            break
        elif arr[middle] > B:
            end = middle
            cntB += 1
        else:
            start = middle
            cntB += 1

    # 갯수 비교
    if cntA > cntB:
        print(f'#{tc} B')
    elif cntA < cntB:
        print(f'#{tc} A')
    elif cntA == cntB:
        print(f'#{tc} 0')
