class Solution:
    def romanToInt(self, s: str) -> int:
        chars: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        flag: bool = False
        total: int = 0

        for i, j in enumerate(s):
            if flag:
                flag = False
                continue

            if i == len(s)-1:
                total += chars[j]
                break

            if chars[j] < chars[s[i+1]]:
                total += chars[s[i+1]] - chars[j]
                flag = True

            else:
                total += chars[j]

        return total