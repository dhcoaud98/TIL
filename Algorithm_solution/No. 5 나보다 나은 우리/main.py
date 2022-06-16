import sys
sys.stdin = open('sample_input.txt')

N = int(input())
ans = list(map(str, input().split()))
student = []
for n in range(N):
    student.append(list(map(str, input().split())))

a = input()
print(ans)
print(student)


def sol(idx, k, p):
    if idx == k:
        print(p)



for i in range(1, N+1):  # 학생 수만큼 진행할 예정
    used = [0] * i
    p = [0] * i
    sol(0, i, p)