# -*- coding:UTF-8 -*-
# 3.6.1
import math

class PlusOne:
    def change(self, array):
        num = 1
        for i in range(len(array)-1, -1, -1):
            a = array[i] + num
            array[i] = a % 10
            num = math.floor(a / 10)
        
        if num == 1:
            array.insert(0, 1)
        return array

plusOne = PlusOne()
array = [5, 6, 2, 5, 9]
newArray = plusOne.change(array)
print(newArray)