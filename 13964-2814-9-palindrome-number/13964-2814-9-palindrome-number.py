class Solution:
    def isPalindrome(self, x: int) -> bool:
        line: str = str(x)
        new_line: str = "".join([i for i in reversed(line)])
        if line == new_line:
            return True
        return False