arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
# 합이 0 이 되는 부분집합 출력

for i in range(1 << n):  # n비트의 이진수 출력, 부분집합의 개수
    zero = 0
    result = []
    for j in range(0, n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번째 비트가 1 이면 j 번째 원소 출력
            # print(arr[j], end='')
            result.append(arr[j])
            zero += arr[j]
    # print()
    if zero == 0:  # 부분집합의 합이 0이라면 출력!!
        print(result)
    # print(zero)
    # print('---')


