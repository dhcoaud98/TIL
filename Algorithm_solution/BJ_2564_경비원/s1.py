import sys
sys.stdin = open('input.txt')

width, height = map(int, input().split())
N = int(input())
Store = []
for i in range(N):
    Store.append(list(map(int, input().split())))

Direction, number = map(int, input().split())
print(Store)
print(Direction, number)
