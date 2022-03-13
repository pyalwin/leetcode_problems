'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

def remove_duplicates(arr):
   itr = 1
   for i in range(len(arr)):
       print(i, itr)
       if arr[i] != arr[itr - 1]:
           arr[itr] = arr[i]
           itr += 1
   return len(arr[:itr])

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))