import sys
sys.stdin = open('input.txt')

width, height = map(int, input().split())
N = int(input())
Store = []
for i in range(N):
    Store.append(list(map(int, input().split())))

Direction, number = map(int, input().split())
# print(Store)
# print(Direction, number)
# 최솟값 구하기
move_count = 0
for i in range(N):
    # 같은 위치
    if Direction == Store[i][0]:
        move_count += abs(number-Store[i][1])
    # 상하
    elif Direction == 1 and Store[i][0] == 2:
        if number + height + Store[i][1] <= (width - number) + height + (width - Store[i][1]):
            move_count += number + height + Store[i][1]
        else:
            move_count += (width - number) + height + (width - Store[i][1])
    elif Store[i][0] == 1 and Direction == 2:
        if number+height+Store[i][1] <= (width-number)+height+(width-Store[i][1]):
            move_count += number+height+Store[i][1]
        else:
            move_count += (width-number)+height+(width-Store[i][1])
    # 좌우
    elif Direction == 3 and Store[i][0] == 4:
        if number+width+Store[i][1] <= (height-number)+width+(height-Store[i][1]):
            move_count += number+width+Store[i][1]
        else:
            move_count += (height-number)+width+(height-Store[i][1])
    elif Store[i][0] == 3 and Direction == 4:
        if number+width+Store[i][1] <= (height-number)+width+(height-Store[i][1]):
            move_count += number+width+Store[i][1]
        else:
            move_count += (height-number)+width+(height-Store[i][1])
    # 인접
    else:
        if Direction == 1 and Store[i][0] == 3:
            move_count += number + Store[i][1]
        elif Store[i][0] == 1 and Direction == 3:
            move_count += number + Store[i][1]

        elif Direction == 1 and Store[i][0] == 4:
            move_count += (width-number) + Store[i][1]
        elif Store[i][0] == 1 and Direction == 4:
            move_count += number + (height-Store[i][1])

        elif Direction == 2 and Store[i][0] == 4:
            move_count += (width-number) + (height-Store[i][1])
        elif Store[i][0] == 2 and Direction == 4:
            move_count += (width-number) + (height-Store[i][1])

        elif Direction == 2 and Store[i][0] == 3:
            move_count += number + (height-Store[i][1])
        elif Store[i][0] == 2 and Direction == 3:
            move_count += (height-number) + Store[i][1]
    
print(move_count)
