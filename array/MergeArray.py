# -*- coding:UTF-8 -*-
class MergeArray:
    def merge(self, arrA, m, arrB, n):
        i = m + n -1
        m -= 1
        n -= 1

        while i >= 0:
            if m >= 0 and n >= 0:
                if arrA[m] > arrB[n]:
                    arrA[i] = arrA[m]
                    m -= 1
                else:
                    arrA[i] = arrB[n]
                    n -= 1
            elif m >= 0:
                arrA[i] = arrA[m]
                m -= 1
            else:
                arrA[i] = arrB[n]
            
            i -= 1

        return arrA

mergeArray = MergeArray()
arrA = [1, 3, 5, 7, 9, 0, 0, 0, 0]
arrB = [2, 4, 6, 8]
arrA = mergeArray.merge(arrA, 5, arrB, 4)
print(arrA)