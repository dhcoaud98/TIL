import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, mystr = map(str, input().split())
    # print(mystr)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    answer = []
    for i in range(1, len(mystr)+1):
        for j in range(len(mystr)):
            if mystr[j:j+i] not in answer:
                answer.append(mystr[j:j+i])

    M = int(N)
    flag = True
    a = 0
    while flag:
        temp = []
        for j in range(len(answer)):
            if answer[j][0] == alphabet[a]:
                temp.append(answer[j])
        a += 1
        if len(temp) >= M:
            result = sorted(temp)
            print(f'#{tc} {result[int(M)-1][0]} {len(result[int(M)-1])}')
            flag = False
        elif len(temp) < M:
            M = M - len(temp)
