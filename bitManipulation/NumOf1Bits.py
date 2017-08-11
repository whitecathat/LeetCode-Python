# 3.6.1
# -*- coding:UTF-8 -*-
class NumOf1Bits:
    def solve(self, num):
        return bin(num).count('1')

numOf1Bits = NumOf1Bits()
print(numOf1Bits.solve(9))