class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff: int = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        