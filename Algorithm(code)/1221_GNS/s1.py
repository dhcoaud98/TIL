import sys

sys.stdin = open('GNS_test_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    # cont의 0번째 인덱스 값은 테스트 케이브 번호, 1번째 인덱스는 케이스 길이
    cont = input().split()
    str1 = input().split()

    change = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    temp = []

    # 0~9까지의 숫자를 찾기 위해
    for i in range(10):  
        for j in range(int(cont[1])):
            # str1의 값이 change의 0번째(ZRO)와 같으면 temp에 append함. 0~9까지 반복
            if str1[j] == change[i]:  
                temp.append(str1[j])

    print(cont[0])
    print(*temp)


