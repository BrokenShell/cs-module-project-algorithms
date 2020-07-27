"""
Input: an integer
Returns: an integer
"""


def fib3(n):
    """ Fibonacci-3 Calculator """
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


def eating_cookies(n, *args):
    """ W(n) = W(n - 1) + W(n - 2) + W(n - 3) """
    return fib3(n+1)


if __name__ == "__main__":
    num_cookies = 100000
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
