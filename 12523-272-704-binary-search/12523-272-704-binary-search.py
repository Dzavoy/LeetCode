class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low: int = 0
        high: int = len(nums) - 1

        while low <= high:
            mid: int = (low + high) // 2
            check: int = nums[mid]
            
            if check == target:
                return mid
            if check > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1