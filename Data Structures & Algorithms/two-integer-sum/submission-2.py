class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            compelement = target - num
            if compelement in seen:
                return [seen[compelement], i]
            seen[num] = i