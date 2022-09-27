import sys
sys.stdin = open('s_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 두개의 수를 골라 곱한 값 구하기
    temp = []
    for i in range(N-1):
        for j in range(i+1, N):
            temp.append(arr[i]*arr[j])
    print(temp)

    # 2. temp를 내림차순하기
    for i in range(len(temp) - 1, 0, -1):  # 범위 설정 주의!
        for j in range(0, i):
            if temp[j] < temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    print(temp)

    # 3. 수가 증가하는지 찾고, 단조 증가하는 수라면 출력하고 break
    for i in temp:
        num = str(i)
        cnt = 0
        for j in range(len(num)-1):
            if num[j] < num[j+1]:
                cnt += 1
        if cnt == len(num)-1:
            max_num = num
            break
    else:
        max_num = -1

    print(f'#{tc} {max_num}')