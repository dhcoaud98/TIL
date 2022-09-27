import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = []
    for _ in range(N):
        n = list(map(int, input().split()))
        arr.append(n)

    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2

    s = 0
    for _ in range(4002):
        # 좌표 이동
        for j in range(len(arr)):
            arr[j][0] += dj[arr[j][2]]
            arr[j][1] += di[arr[j][2]]

        # 좌표 중복되면 삭제
        ddel, V = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj, ci) in V:
                ddel.add((cj, ci))
            V.add((cj, ci))

        # 삭제 리스트에 있으면 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                s += arr[i][3]
                arr.pop(i)

        if len(arr) < 2:
            break

    print(f'#{tc} {s}')
