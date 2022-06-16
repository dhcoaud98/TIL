import sys
sys.stdin = open('input.txt')


def pre(v):  # 전위
    if v:
        print(v)
        pre(ch1[v])
        pre(ch2[v])


def in_order(v):  # 중위
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])


def post(v):  # 후위
    if v:
        post(ch1[v])
        post(ch2[v])
        print(v)


N = int(input())
arr = list(map(int, input().split()))
print(arr)

ch1 = [0]*15
ch2 = [0]*15
for i in range(0, len(arr), 2):
    if ch1[arr[i]] == 0:
        ch1[arr[i]] = arr[i+1]
    else:
        ch2[arr[i]] = arr[i+1]

print(ch1)
print(ch2)
print('전위')
pre(1)
print('중위')
in_order(1)
print('후위')
post(1)
