# 선택정렬을 재귀적으로 풀이


def selectionSort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selectionSort(xs)
    else:
        return []

xs = [5, 2, 6, 3, 7, 1]
print(selectionSort(xs))