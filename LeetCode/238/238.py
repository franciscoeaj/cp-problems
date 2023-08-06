from functools import reduce

# TLE - maybe this slice approach is too slow? nums.length <= 10^5
# maybe think of some way of memoizing the reduces could make it faster?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            arrayExceptSelf = nums[:i] + nums[i + 1:]
            res.append(reduce(lambda x, y: x*y, arrayExceptSelf))

        return res