import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = list(map(int,input().split()))

    # 원소의 개수
    n = len(arr)
    answer = []
    answer1 = []

    # 1. 부분집합 구하기
    for i in range(1 << n):  # 부분 집합의 개수만큼 돈다.
        temp = []
        for j in range(n):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                temp.append(arr[j])
        answer.append(temp)
    
    # 2. 이차원 배열안 리스트의 합을 구해 일차원 리스트로 만들기
    # [[],[],..., []] -> [ , , ..., ]
    for a in range(1, len(answer)):
        my_sum = 0
        for k in range(0, len(answer[a])):
            my_sum += answer[a][k]
        answer1.append(my_sum)

    # 공집합은 answer1[0]에 0으로 있으므로 인덱스 1부터 사용한다.
    for m in answer1[1:]:
        if m == 0:
            result = 1
            break
        else:
            result = 0

    print(f'#{tc} {result}')
