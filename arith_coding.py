import collections
import math
import numpy as np


class Char:
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability
        self.code = None

    def __lt__(self, other):
        return True if self.probability < other.get_probability() else False

    def __str__(self):
        return '{0}\t{1:.2f}\t{2}'.format(self.name, self.probability, self.code)

    def get_name(self):
        return self.name

    def get_probability(self):
        return self.probability

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code


def is_power_of_two(n):
    logn = math.log(n, 2)
    return logn == int(logn)


def find_numbers(low, high):
    for i in np.arange(round(low, 2) + 0.01, round(high, 2) - 0.01, 0.01):
        for j in range(1, 33):
            if is_power_of_two(j):
                for k in range(1, 100):
                    if math.fabs((k / j) - i) <= 0.01:
                        return k, j


def float_to_binary(num):
    exponent=0
    shifted_num=num
    while shifted_num != int(shifted_num):
        shifted_num*=2
        exponent+=1
    if exponent==0:
        return '{0:0b}'.format(int(shifted_num))
    binary='{0:0{1}b}'.format(int(shifted_num),exponent+1)
    integer_part=binary[:-exponent]
    fractional_part=binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part, fractional_part)


def get_fractional(arg):
    fractional_part = str(arg).split('.')[1]
    return fractional_part


def main():
    word = str(input())
    ln_word = len(word)
    lst = []
    for k, v in collections.Counter(word).items():
        p = ((v * 100) / ln_word) / 100
        lst.append(Char(k, p))

    low = 0
    high = 0
    for i in range(len(lst)):
        high += lst[i].get_probability()

        a, b = find_numbers(low, high)
        print("[{}; {}]\t{} / {} = {}".format(low, high, a, b, a/b))
        code = get_fractional(float_to_binary(a / b))
        lst[i].set_code(code)

        low += lst[i].get_probability()

    print()
    for i in lst:
        print(i)

    h_x = 0
    ml = 0
    for i in range(len(lst)):
        h_x += lst[i].get_probability() * math.log2(lst[i].get_probability())
        ml += lst[i].get_probability() * len(lst[i].get_code())
    h_x = -h_x

    print('\nH(x) = {0:.2f}\nML = {1:.2f}'.format(h_x, ml))


if __name__ == '__main__':
    main()
