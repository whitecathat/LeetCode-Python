# 3.6.1
# -*- coding:UTF-8 -*-
class LargestRectangle:
    def solve(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1 ))
        return area

largestRectangle = LargestRectangle()
area = largestRectangle.solve([2, 1, 5, 6, 2, 3])
print(area)