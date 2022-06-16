def solution(s):
    answer = ''

    change = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9}
    alph = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word = ''
    for i in range(len(s)):
        if s[i].isdecimal():
            answer += str(s[i])
        elif s[i].isalpha():
            word += s[i]
            if word in alph:
                answer += str(change[word])
                word = ''
    result = int(answer)
    return result


s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"
print(solution(s))