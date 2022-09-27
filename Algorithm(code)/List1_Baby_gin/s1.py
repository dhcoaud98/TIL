# TC는 테스트 케이스, N은 자리수, num은 주어진 수
TC = 1
N = 6
num = 773457

# -----------------------
# 1. num 값의 숫자별 갯수를 구하여 리스트만들기
c = [0]*12

for i in range(N):
    c[num % 10] += 1
    num //= 10
# print(c)
# [0, 0, 0, 1, 1, 1, 0, 3, 0, 0, 0, 0]

# -----------------------
# 2. triplete와 run 데이터 조사하기
i = 0
tri = run = 0

while i < 10:
    # triplete 구하기
    if c[i] >= 3:
        tri += 1
        c[i] -= 3
        continue
    # run 구하기
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 :
        run += 1
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        continue
    i+=1

if tri+run == 2:
    print("Baby Gin!")
else:
    print("Lose")