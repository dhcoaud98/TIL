import sys
sys.stdin = open('sample_input.txt')

def quick_sort(arr, start,end):
    def partition(start, end):
        pivot = arr[end]
        left = start
        for right in range(start, end):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[end] = arr[end], arr[left]
        return left
    if start < end:
        pivot = partition(start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot+1, end)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)  # 배열, left, right
    print(f'#{tc} {arr[N // 2]}')  # N//2 원소 출력