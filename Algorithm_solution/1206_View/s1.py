import sys

sys.stdin = open('input.txt')

# test case의 길이 = 10으로 주어졌다.
Tc = 10

# 계산을 위해 for문 사용
for tc in range(1, Tc+1):
    result = 0
    width = list(map(int, input().split()))      # 각각의 text case의 가로 길이
    case1 = list(map(int, input().split()))      # 그 다음 줄의 col별로 높이를 list화 하기
    news = []                                    # 새로운 list를 만들기 위해 초기화

    # list를 인덱스로 접근한다. list의 길이는 width로 구해져 있음.
    for i in range(2, width[0]-2):
        # list[0:5], list[1:6], ...., 별로 list화 하기
        news.append(case1[i-2:i+3])

    # news의 인덱스로 접근한다.
    for new in news:
        empty_list = []
        a = new[2] - new[1]
        b = new[2] - new[0]
        c = new[2] - new[3]
        d = new[2] - new[4]
        # 값 비교를 위해 cnt에 a 값을 넣음
        cnt = a 

        if a >= 1 and b >= 1 and c >= 1 and d >= 1:
            empty_list = [a, b, c, d]
            # 가운데 빌딩의 높이와 양 옆 네개의 빌딩의 차를 리스트 한 값 중 가장 작은 값을 cnt에 넣음
            for m in empty_list:
                if m < cnt:
                    cnt = m
            result += cnt

    print(f'#{tc} {result}')
