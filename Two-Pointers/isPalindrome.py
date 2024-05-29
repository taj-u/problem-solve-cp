'''
  author: Taj Uddin (CSE08@BSMRSTU)
  github: https://www.github.com/taj-u
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for ch in s:
            # check if the character is alphanum
            if (ch >= 'a' and ch <= 'z') or (ch >='A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
                st += ch
        i, j, flag, st = 0, len(st) - 1, True, st.lower()
        # print(st)
        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True

# https://neetcode.io/problems/is-palindrome