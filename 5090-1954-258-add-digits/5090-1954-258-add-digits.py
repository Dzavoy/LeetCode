class Solution:
    def addDigits(self, num: int) -> int:
        digit: int = num
        while digit > 9:
            nums: list[int] = [int(i) for i in str(digit)]
            digit = sum(nums)
        return digit
        