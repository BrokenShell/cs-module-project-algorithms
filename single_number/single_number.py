"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""
from collections import Counter


def single_number(arr):
    return Counter(arr).most_common()[-1][0]


if __name__ == '__main__':
    array = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    print(f"The odd-number-out is {single_number(array)}")
