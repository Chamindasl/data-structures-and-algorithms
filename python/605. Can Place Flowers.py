# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # base
        if n == 0: return True
        if n > len(flowerbed): return False
        prev_1 = -1
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                gaps = i - prev_1 - 1
                if gaps >= 1:
                    div, mod = divmod(gaps, 2)
                    count += (div + mod - 1) if prev_1 >=0 else div
                    if count >= n: return True
                prev_1 = i

        gaps = len(flowerbed) - prev_1 - 1
        if gaps >= 1:
            div, mod = divmod(gaps, 2)
            count += div if prev_1 >= 0 else (div + mod)
            if count >= n: return True
        return False
