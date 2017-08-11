# 3.6.1
# -*- coding:UTF-8 -*-
class PowerOfTwo:
    def solve(self, num):
        return num > 0 and not (num & (num-1))
    
powerOfTwo = PowerOfTwo()
print(powerOfTwo.solve(3))
print(powerOfTwo.solve(4))

'''
def solve(self, num):
    return num > 0 and (num % 2 == 0)
'''
                