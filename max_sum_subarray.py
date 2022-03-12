'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sum_subarray(arr, k):
  max_sum = 0
  start, end = 0, k

  while end < len(arr):
    max_sum = max(sum(arr[start:end]), max_sum)
    start += 1
    end += 1

  return max_sum
  
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print(max_sum_subarray([2, 3, 4, 1, 5], 2))
print(max_sum_subarray([2, 3], 3))
print(max_sum_subarray([2, 3, 4, 5, 6, 6, 5], 3))
