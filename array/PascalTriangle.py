# -*- coding:UTF-8 -*-

class PascalTriangle:
    def draw(self, n):
        array = []
        for i in range(n):
            array.append([1])
            for j in range(1, i+1):
                if j == i:
                    array[i].append(1)
                else:
                    array[i].append(array[i-1][j-1] + array[i-1][j])
        return array

pascalTriangle = PascalTriangle()
array = pascalTriangle.draw(6)
print(array)
