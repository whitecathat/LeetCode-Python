# 3.6.1
# -*- coding:UTF-8 -*-
import operator
from functools import reduce

class MissingNum:
    def solve(self, arr):
        a = reduce(operator.xor, arr)
        b = reduce(operator.xor, range(len(arr) + 1))
        return a ^ b

nums = [0, 1, 2, 3, 5, 6]
missingNum = MissingNum()
print(missingNum.solve(nums))

'''
    def solve(self, arr):
        n = len(arr)
        return n * (n + 1) / 2 - sum(arr)
'''