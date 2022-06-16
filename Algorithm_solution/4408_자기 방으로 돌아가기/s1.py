import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = [0]*200  # 동선
    N = int(input())

    temp = answer = []
    for k in range(N):
        temp = []
        A, B = map(int, input().split())
        # 1. 만약 큰 수에서 작은 수로 돌아간다면 A와 B의 위치를 바꿈
        if A > B:
            A, B = B, A
            
        # 2-1. A가 홀수
        if A % 2 == 1:
            # 2-1-1. B는 홀수
            if B % 2 == 1:
                for j in range(A, B+1, 2):
                    arr[j//2] += 1
            # 2-1-2. B는 짝수
            else:
                for j in range(A, B, 2):
                    arr[j//2] += 1
        # 2-2. A가 짝수
        else:
            # 2-2-1. B는 짝수
            if B % 2 == 0:
                for j in range(A, B+1, 2):
                    arr[j//2 - 1] += 1
            # 2-2-2. B는 홀수
            else:
                for j in range(A, B, 2):
                    arr[j//2 - 1] += 1
                arr[B//2] += 1

    # 3. 최댓값 찾기
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i] >= max_num:
            max_num = arr[i]
    
    print(f'#{tc} {max_num}')