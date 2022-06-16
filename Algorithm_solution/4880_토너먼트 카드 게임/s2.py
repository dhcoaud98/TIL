import sys
sys.stdin = open('sample_input.txt')

# 2. 가위바위보 조건 만들기
def win(my_list, l_idx, r_idx):
    # win이라는 함수는 관찰하는 값이 인덱스이므로 인덱스만을 반환하게 한다.
    # 조건은 리스트의 해당 인덱스의 값으로 비교한다.
    if my_list[l_idx] == 1:  # 리스트의 왼쪽 같이 1(가위)라면
        if my_list[r_idx] == 1 or my_list[r_idx] == 3:  # 오른쪽이 1(가위) 혹은 3(보자기)라면 왼쪽의 승리이므로 왼쪽 인덱스 가져오기
            return l_idx
        else:  # 오른쪽이 2(주먹) 이라면 오른쪽 인덱스 가져온다.
            return r_idx
    elif my_list[l_idx] == 2:
        if my_list[r_idx] == 3:
            return r_idx
        else:
            return l_idx
    else:
        if my_list[r_idx] == 1:
            return r_idx
        else:
            return l_idx


# 1. 실제 게임을 하는 함수이다.
def game(my_list, start, end):
    # 1. start와 end가 같다면 재귀함수 호출을 멈춘다.
    # 2. 왼쪽과 오른쪽으로 나누고, 이 것을 재귀함수로 불러냄
    # 3. 왼쪽과 오른쪽으로 나눈 후 각각의 이긴 인덱스를 불러낼 수 있도록 함수를 만든다.
    # !! 함수는 return 값으로 지정해주는데 return 값이 없다면 이전 값과 동일하다.
    if start == end:
        return start
    left = game(my_list, start, (start + end) // 2)
    right = game(my_list, (start + end) // 2 + 1, end)
    return win(my_list, left, right)

# 1. main에서 input 받고, 함수 부르기
TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    student = list(map(int, input().split()))
    result = game(student, 0, N - 1)  # list와, 시작점, 끝점!
    print(f"#{tc} {result + 1}")