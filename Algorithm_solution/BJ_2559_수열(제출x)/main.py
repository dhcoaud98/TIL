import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_num = 0
for i in range(N-K+1):
    if sum(arr[i:i+K]) >= max_num:
        max_num = sum(arr[i:i+K])

print(max_num)
