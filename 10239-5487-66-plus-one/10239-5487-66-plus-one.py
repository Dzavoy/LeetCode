class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        chars: list[str] = [str(i) for i in digits]
        addition: int = int("".join(chars)) + 1
        line: str = str(addition)

        return [int(i) for i in line]