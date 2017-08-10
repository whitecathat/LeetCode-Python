# -*- coding:UTF-8 -*-
# 3.6.1
import math
class FindNum:
    def solve(self, arr):
        length = len(arr)
        if length == 0:
            return 0
        elif length == 1:
            return arr[0]
        elif length == 2:
            return min(arr[0], arr[1])

        start = 0
        end = length - 1
        while start < end - 1:
            if arr[start] < arr[end]:
                return arr[start]
            mid = start + math.floor((end - start)/2)
            if arr[mid] > arr[start]:
                start = mid
            else:
                end = mid
        return min(arr[start], arr[end])

findNum = FindNum()
arr = [4, 5, 6, 7, 1, 2, 3]
num = findNum.solve(arr)
print(num)