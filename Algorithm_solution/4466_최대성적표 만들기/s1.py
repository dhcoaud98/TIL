import sys
sys.stdin =  open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))


    # 성적 내림차순 버블정렬
    for i in range(N-1):
        for j in range(N-(i+1)):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    result = 0
    for k in range(K):
        result += arr[k]

    print(f'#{tc} {result}')