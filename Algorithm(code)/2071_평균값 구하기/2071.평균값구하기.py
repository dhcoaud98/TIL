import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_sum = 0
    my_len = 0
    nums = list(map(int, input().split()))
    # print(nums)
    for num in nums:
        my_sum += num
        my_len += 1

    result = round(my_sum / my_len)

    print(f'#{tc} {result}')