import sys
sys.stdin=open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    dec = float(input())
    n = 1
    cnt = 0
    result = ''
    
    while True:
        cnt += 1
        n *= 0.5
        if dec - n >= 0:  # 0.5**x (x는 소수 몇번째 자리인지) 를 뺐을 때 0보다 크면
            result += '1'
            dec -= n
            if dec == 0:
                break
        else:  # 0.5**x를 뺏을 때 0보다 작으면
            result += '0'
        if cnt >= 13:  # 소수점 13자리 이상으로 넘어갈 때 종료
            result = 'overflow'
            break

    print(f'#{tc} {result}')