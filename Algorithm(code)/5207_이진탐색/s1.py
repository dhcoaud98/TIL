import sys
sys.stdin = open('sample_input.txt')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort()  # 정렬하지 않으면 fail
    B_list = list(map(int, input().split()))
    result = 0

    for B in B_list:
        if B in A_list:
            low = 0
            high = N - 1
            direct = 0  # 방향 탐색
            while low <= high:
                mid = (low+high) // 2

                if A_list[mid] == B:
                    result += 1
                    break

                elif A_list[mid] > B:
                    high = mid - 1
                    if direct == 1:
                        break
                    direct = 1

                else:
                    low = mid + 1
                    if direct == -1:
                        break
                    direct = -1

    print(f'#{tc} {result}')
