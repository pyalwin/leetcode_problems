'''
Problem Statement 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''

import bisect

def sorting_squares(arr):
  i,j = 0, len(arr)-1
  res = []
  while (i<=j):
    if abs(arr[i]) > abs(arr[j]):
       res = [arr[i]**2] + res
       i += 1
    else:
       res = [arr[j]**2] + res
       j -= 1

  return res

print(sorting_squares([-2, -1, 0, 2, 3]))
print(sorting_squares([-3, -1, 0, 1, 2]))