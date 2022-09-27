import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:  # 배열의 길이가 1이하이면 arr을 return
        return arr

    pivot = arr[len(arr)//2]  # 중간 값을 pivot로 설정
    """
    low_arr은 왼편의 작은 값
    high_arr은 오른편의 큰 값
    equal_arr은 pivot의 값과 같은 값
    """

    low_arr, equal_arr, high_arr = [], [], []
    # 11, 45, 23, 81, 28, 34
    for num in arr:
        if num < pivot:  # num이 pivot보다 작으면
            low_arr.append(num)
        elif num > pivot:  # num이 pivot보다 크면
            high_arr.append(num)
        else:  # num이 pivot과 같으면
            equal_arr.append(num)

    return quick_sort(low_arr) + equal_arr + quick_sort(high_arr)


for tc in range(3):
    arr = list(map(int, input().split(', ')))
    print('Input : ', arr)
    print('Quick_sort : ', quick_sort(arr))
