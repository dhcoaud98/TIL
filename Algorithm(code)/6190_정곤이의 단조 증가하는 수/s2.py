import sys
sys.stdin = open('s_input.txt')

TC = int(input())

def f(N):
    global arr, temp, max_num

    for i in range(N-1):
        for j in range(i+1, N):
            num = str(arr[i]*arr[j])
            for k in range(len(num) - 1):
                if num[k] < num[k + 1]:  # 단조일 경우 넘어감
                    pass
                else:  # 단조가 아닐 경우 종료
                    break
            else:  # num을 끝까지 조사했는데 단조일 경우
                if int(num) >= max_num:
                    max_num = int(num)

    return max_num

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    temp = []
    max_num = -1
    print(f'#{tc} {f(N)}')
