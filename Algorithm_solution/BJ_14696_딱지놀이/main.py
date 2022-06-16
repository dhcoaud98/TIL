import sys
sys.stdin = open('input2.txt')

# 별, 동그라미, 네모, 세모를  4, 3, 2, 1로 표현(숫자가 높은 것이 이김)
N = int(input())

for n in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = A[1:]
    B = B[1:]
    # print(A, B)

    # 1. 카운팅 정렬하기
    temp_A = [0] * 5
    temp_B = [0] * 5
    for i in range(len(A)):
        temp_A[A[i]] += 1

    for i in range(len(B)):
        temp_B[B[i]] += 1
    # print(temp_A, temp_B)

    # 2. 비교하기
    now = 4
    result = 'D'
    if temp_A == temp_B:
        result = 'D'
    else:
        while now > 0:
            if temp_A[now] == temp_B[now]:
                now -= 1
            elif temp_A[now] > temp_B[now]:
                result = 'A'
                break
            else:
                result = 'B'
                break

    print(result)
