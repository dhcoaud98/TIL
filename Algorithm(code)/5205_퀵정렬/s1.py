import sys
sys.stdin = open('sample_input.txt')


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    low_arr, equal_arr, high_arr = [], [], []
    for num in arr:
        if num < pivot:
            low_arr.append(num)
        elif num > pivot:
            high_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(low_arr) + equal_arr + quick_sort(high_arr)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(arr)[N//2]}')
