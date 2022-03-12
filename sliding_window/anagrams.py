'''
String Anagrams
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

from collections import Counter

def get_anagrams(s, p):
    pt_cnt = Counter(p)
    res = None

    for i in range(len(s)):
       curr_rec = i
       while curr_rec + len(p) <= len(s):
           tmp_cnt = Counter(s[curr_rec:curr_rec+len(p)])
           if tmp_cnt == pt_cnt:
              res = list(range(curr_rec,curr_rec+len(p)))
              break
           curr_rec += 1
       if res:
         return res

    return res

print(get_anagrams("ppqp","pq"))
print(get_anagrams("abbcabc","abc"))
