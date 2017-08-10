# -*- coding:UTF-8 -*-
class RemoveElement:
    def remove(self, oldArray, elem):
        j, n = 0, 0

        for i in range(0, len(oldArray)):
            if oldArray[i] == elem:
                n += 1
                continue
            oldArray[j] = oldArray[i]
            j += 1

        for i in range(len(oldArray)-1, len(oldArray)-1-n, -1):
            oldArray.pop(i)

        return oldArray

removeElement = RemoveElement()
oldArray = [1, 3, 5, 7, 9, 11, 11, 25, 17]
newArray = removeElement.remove(oldArray, 25)
print(newArray)

