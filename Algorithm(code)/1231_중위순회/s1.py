import sys
sys.stdin=open('input.txt')


# 중위
def in_order(v):
    global alphabet
    if v:  # 0번 정점이 없으므로 0번은 자식이 없는 경우를 표시
        in_order(ch1[v])
        print(alphabet[v-1][1], end='')
        in_order(ch2[v])

for tc in range(1, 11):
    N = int(input())
    # 이진트리 이기 때문에 자식 리스트 두개 생성
    ch1 = [0] * (N+2)
    ch2 = [0] * (N+2)
    alphabet = []

    for n in range(N):
        TEMP = input().split()
        # 1. 부모 번호를 인덱스로 자식 번호 저장
        if len(TEMP) == 4:
            ch1[int(TEMP[0])] = int(TEMP[2])
            ch2[int(TEMP[0])] = int(TEMP[3])
        elif len(TEMP) == 3:
            ch1[int(TEMP[0])] = int(TEMP[2])
        # 2. 정점과 알파벳 연결해서 리스트 만들기
        alphabet.append([TEMP[0], TEMP[1]])

    print(f'#{tc}', end=' ')
    in_order(1)
    print()
