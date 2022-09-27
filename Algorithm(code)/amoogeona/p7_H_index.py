def solution(citations):
    answer = 0
    for i in range(len(citations), -1, -1):
        low_num, high_num = 0, 0
        for c in citations:
            if c >= i:
                high_num += 1
            if c <= i:
                low_num += 1
        if high_num >= i:
            answer = i
            break
    return answer

# citations = [3, 0, 6, 1, 5]
# citations = [10,10,10,10,10]
citations = [0, 0, 0, 0, 0]
print(solution(citations))