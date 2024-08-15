'''
  author: Taj Uddin (CSE08@BSMRSTU)
  github: https://www.github.com/taj-u
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, size = 0, len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                if ((i == 0) or (flowerbed[i-1] == 0)) and ((i + 1 == size) or (flowerbed[i+1] == 0)):
                    count += 1
                    flowerbed[i] = 1  
        if count >= n:
            return True
        else:
            return False

# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75