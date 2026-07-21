class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to scan the table and compute the complement
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num]=i
            
        