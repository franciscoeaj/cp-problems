class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in range(len(candies)):
            totalCandies = candies[i] + extraCandies

            if totalCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)

        return results