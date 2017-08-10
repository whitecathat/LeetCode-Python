# -*- coding:UTF-8 -*-
class RemoveDuplicates:
    def remove(self, sortedArray):
        if len(sortedArray) == 0:
            return 0

        j, n = 0, 0
        for i in range(1, len(sortedArray)):
            if sortedArray[j] != sortedArray[i]:
                j += 1
                sortedArray[j] = sortedArray[i]
            else:
                n += 1
        
        for i in range(len(sortedArray)-1, len(sortedArray)-1-n, -1):
            sortedArray.pop(i)
        
        return len(sortedArray)

removeDuplicates = RemoveDuplicates()
oldArray = [1, 3, 5, 7, 9, 11, 11, 25, 17]
print(removeDuplicates.remove(oldArray))