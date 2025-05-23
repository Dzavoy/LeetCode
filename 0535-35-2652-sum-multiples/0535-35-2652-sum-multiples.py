class Solution:
    def sumOfMultiples(self, n: int) -> int:
        numbers: list[int] = list(range(1, n+1))
        check: list[int] = [
            i for i in numbers
            if i%3 == 0 
            or i%5 == 0
            or i%7 == 0
        ]
        
        return sum(check)