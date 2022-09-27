import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    student = list(map(str, input().split()))
    # 리스트 접근을 위해  str로 불러옴. 계산 시에는 int로 바꿔주기!
    temp = []
    print(student)

    start = 0
    end = N
    stack1 = []
    stack2 = []

    # 처음에 두 부분으로 나눔
    middle = N // 2
    # ['1', '3', '3', '3', '1', '1', '3']
    # [['1', '3', '3'], ['3', '1', '1', '3']]

    if middle % 2:  # 홀수명
        for i in range(0, middle):  # 왼쪽에서 승자 가리기
            
        for i in range(middle, N):  # 오른쪽에서 승자 가리기
            pass
    else:  # 짝수명
        for i in range(0, middle):  # 왼쪽에서 승자 가리기
            pass
        for i in range(middle, N):  # 오른쪽에서 승자 가리기
            pass


    # stack1.append(student[:middle])
    # stack1.append(student[middle:])
    # print(stack1)
