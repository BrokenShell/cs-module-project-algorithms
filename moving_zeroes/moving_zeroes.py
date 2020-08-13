"""
Input: a List of numbers
Returns: a List of numbers
"""


def moving_zeroes(arr):
    return [num for num in arr if num != 0] + [0] * arr.count(0)


if __name__ == '__main__':
    some_list = [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(some_list)}")
