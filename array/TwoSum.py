# -*- coding:UTF-8 -*-
# py3 doesn't have has_key function
class TwoSum:
    def solve(self, arr, num):
        dict = {}
        for i in range(len(arr)):
            dict[arr[i]] = i
        for i in range(len(arr)):
            val = num - arr[i]
            if val in dict:
                if i == dict[val]:
                    continue
                elif dict[val] > i:
                    return [i+1, dict[val]+1]
                else:
                    return [dict[val]+1, i+1]

twoSum = TwoSum()
arr = [1, 4, 5, 6, 7]
ret = twoSum.solve(arr, 8)
print(ret)