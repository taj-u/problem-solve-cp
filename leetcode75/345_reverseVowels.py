'''
  author: Taj Uddin (CSE08@BSMRSTU)
  github: https://www.github.com/taj-u
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in vowel:
                i += 1
            elif s[j] not in vowel:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75