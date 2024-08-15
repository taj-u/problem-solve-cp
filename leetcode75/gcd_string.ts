/* 
    author: Taj Uddin (CSE08@BSMRSTU)
    github: https://www.github.com/taj-u
*/


function gcdOfStrings(str1: string, str2: string): string {
  let gcd = function (a, b) {
    if (b == 0) return a;
    return gcd(b, a % b);
  };
  if (str1 + str2 !== str2 + str1) return "";
  return str1.slice(0, gcd(str1.length, str2.length));
}

// https://leetcode.com/problems/greatest-common-divisor-of-strings/description/