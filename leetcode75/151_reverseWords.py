'''
  author: Taj Uddin (CSE08@BSMRSTU)
  github: https://www.github.com/taj-u
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = list(reversed(s))  // s[::-1]
        return ' '.join(s)

# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75