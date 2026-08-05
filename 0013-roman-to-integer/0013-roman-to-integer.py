class Solution(object):
    def romanToInt(self, s):
        total = 0
        roman = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000,
        }
        for i, char in enumerate(s):
            if i + 1 < len(s) and roman[s[i + 1]] > roman[char]:
                total -= roman[char]
            else:
                total += roman[char]

        return total