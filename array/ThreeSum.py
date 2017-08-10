# -*- coding:UTF-8 -*-

class ThreeSum(object):
    def solve(self, arr):
        length = len(arr)
        resultList = []
        arr.sort()
        for i in range(0, length-2):
            j = i + 1
            k = length - 1
            while j < k:
                sum = arr[i] + arr[j] + arr[k]
                if sum == 0:
                    result = []
                    result.append(arr[i])
                    result.append(arr[j])
                    result.append(arr[k])
                    if result not in resultList:
                        resultList.append(result)
                    j +=1
                elif sum < 0:
                    j +=1
                else:
                    k -=1
        return resultList

threeSum = ThreeSum()
arr = [-1, -1, 2, -3, 3, 0]
ret = threeSum.solve(arr)
print(ret)