from itertools import combinations_with_replacement, permutations


def rock_paper_scissors(n):
    group = ['rock', 'paper', 'scissors']
    if n == 0:
        return [[]]
    else:
        combos = combinations_with_replacement(group, n)
        result = set()
        for arr in combos:
            for itm in permutations(arr, n):
                result.add(itm)
        result = list(map(list, result))
        for i in range(n, 0, -1):
            result.sort(key=lambda x: group.index(x[i - 1]))
        return result
