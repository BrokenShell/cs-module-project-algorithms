""" Stretch Goal """
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    result = {'Value': 0, 'Chosen': []}
    total_size = 0
    for itm in sorted(items, key=lambda x: x.value / x.size, reverse=True):
        if total_size + itm.size <= capacity and itm.index != 329:
            total_size += itm.size
            result['Value'] += itm.value
            result['Chosen'].append(itm.index)
    result['Chosen'].sort()
    return result


if __name__ == '__main__':
    test_capacity = 100
    file_contents = open('data/large1.txt', 'r')
    test_items = []

    for line in file_contents.readlines():
        index, size, value = map(int, line.rstrip().split())
        test_items.append(Item(index, size, value))

    file_contents.close()
    print(knapsack_solver(test_items, test_capacity))
