import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, mystr = map(str, input().split())
    # print(mystr)
    answer = []
    for i in range(1, len(mystr)+1):
        for j in range(len(mystr)):
            if mystr[j:j+i] not in answer:
                answer.append(mystr[j:j+i])
    answer = sorted(answer)
    # print(answer)

    print(f'#{tc} {answer[int(N)-1][0]} {len(answer[int(N)-1])}')