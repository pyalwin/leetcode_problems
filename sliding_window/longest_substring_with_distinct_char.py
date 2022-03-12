'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

def longest_distinct_substring(s,k):
   s_str = ''
   counts = {}
   for i in range(len(s)):
       rec = i
       while rec < len(s):
            if s[rec] in counts:
                counts[s[rec]] += 1
            elif s[rec] not in counts and len(counts) < k:
                 counts[s[rec]] = 1
            else:
              break
            rec += 1
       print(counts, i, rec, s[i:rec])
       if len(s[i:rec]) > len(s_str):
           s_str = s[i:rec]
   print(s_str)
   return len(s_str)

print(longest_distinct_substring('araaci', 2))
print(longest_distinct_substring('araaci', 1))
print(longest_distinct_substring('cbbebi', 4))