class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        capacity = 0
        for i in range(len(flowerbed)):
            cur_bed_empty = flowerbed[i] == 0
            next_bed_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            prev_bed_empty = i == 0 or flowerbed[i - 1] == 0

            if cur_bed_empty and next_bed_empty and prev_bed_empty:
                flowerbed[i] = 1
                capacity += 1
            
        return capacity >= n
