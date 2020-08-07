import sys


def making_change(amount, denominations):
    table = [0 for _ in range(amount + 1)]
    table[0] = 1
    for i in range(len(denominations)):
        for j in range(denominations[i], amount + 1):
            table[j] += table[j - denominations[i]]
    return table[amount]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = [1, 5, 10, 25, 50]
        a = int(sys.argv[1])
        print(f"There are {making_change(a, d)} ways to make {a} cents.")
    else:
        print("Usage: making_change.py [amount]")
