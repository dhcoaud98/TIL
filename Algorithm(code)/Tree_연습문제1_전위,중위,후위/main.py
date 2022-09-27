import sys
sys.stdin = open('input.txt')

# 전위
def pre_order(v):
    if v:  # 0번 정점이 없으므로 0번은 자식이 없는 경우를 표시
        print(v)
        pre_order(ch1[v])
        pre_order(ch2[v])

# 중위
def in_order(v):
    if v:  # 0번 정점이 없으므로 0번은 자식이 없는 경우를 표시
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])

# 후위
def post_order(v):
    if v:  # 0번 정점이 없으므로 0번은 자식이 없는 경우를 표시
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)




E = int(input())  # 정점의 수
arr = list(map(int, input().split()))
V = E + 1  # 정점의 수 == 1번부터 V번까지 정점이 있을 때 마지막 정점

# 부모 번호를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(len(arr)//2):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:  # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c

print(ch1)
print(ch2)
print('전위')
pre_order(1)
print('중위')
in_order(1)
print('후위')
post_order(1)
