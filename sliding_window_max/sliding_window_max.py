"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(arr, k):
    groups = []
    prev_max = None
    for i in range(1 + len(arr) - k):
        if i != 0 and prev_max != arr[i - 1]:
            prev_max = max((prev_max, arr[i + k - 1]))
        else:
            prev_max = max(arr[i: i + k])
        groups.append(prev_max)
    return groups


if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
