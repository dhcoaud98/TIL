import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    string = input()

    # stack 사용
    # 첫번째 문자를 넣고 시작하기
    temp = [string[0]]
    for i in range(1, len(string)):
        # 만약 빈 temp라면 문자 넣기
        if temp == []:
            temp.append(string[i])
        # 입력이 이전과 동일하지 않은 경우 문자 append 
        elif temp[-1] != string[i]:
            temp.append(string[i])
        # 입력이 이전과 동일한 경우 둘다 삭제    
        elif temp[-1] == string[i]:
            temp.pop()

    print(f'#{tc} {len(temp)}')