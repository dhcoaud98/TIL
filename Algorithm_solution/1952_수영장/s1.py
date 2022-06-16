import sys
sys.stdin = open('sample_input.txt')

def DFS(n):
    global price, price_now
    
    if n <= 12 and calendar[n] == 0:
        DFS(n+1)
    elif n >= 13:  # 12월까지 모두 순회 했지만 가격이 싸지 않다면 return
        if price_now < price:
            price = price_now
    else:
        # 1년짜리
        price_now += pays[3]
        DFS(n+13)
        price_now -= pays[3]
        
        # 3개월 짜리
        price_now += pays[2]
        DFS(n+3)
        price_now -= pays[2]
        
        # 1개월 짜리
        price_now += pays[1]
        DFS(n+1)
        price_now -= pays[1]

        price_now += pays[0]*calendar[n]
        DFS(n+1)
        price_now -= pays[0] * calendar[n]

TC = int(input())
for tc in range(1, TC+1):
    pays = list(map(int, input().split()))
    calendar = [0]+list(map(int, input().split())) + [0, 0, 0]

    # 1일권의 갯수
    price = 365 * pays[0]  # 가격을 일일권을 사용했을 때로 맞추기
    price_now = 0
    now_cnt = 0  # 지금 현재의 달
    # print(max_count)
    DFS(now_cnt)
    print(f'#{tc} {price}')