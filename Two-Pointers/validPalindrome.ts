//   author: Taj Uddin (CSE08@BSMRSTU)
//   github: https://www.github.com/taj-u

function isPalindrome(s: string): boolean {
  let st = '';

  // Check for alphanumeric characters (case-insensitive)
  for (const ch of s) {
    if (/\w/i.test(ch) && ch != '_') {
      st += ch.toLowerCase(); 
    }
  }

  let i = 0;
  let j = st.length - 1;

  // Two-pointer approach for palindrome check
  while (i < j) {
    if (st[i] !== st[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true; 
};

// https://leetcode.com/problems/valid-palindrome/