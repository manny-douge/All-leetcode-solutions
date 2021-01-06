#Given a column title as appear in an Excel sheet, return its corresponding
#column number.
#
#For example:
#
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#Example 1:
#
#Input: "A"
#Output: 1

class Solution:
    def titleToNumber(self, s: str) -> int:
        power = 0
        base = 26
        total_value = 0
    
        i = len(s)-1
        while i >= 0:
            value = ord(s[i]) - 64
            total_value += value * (base **power)
            power += 1

            i -= 1
        return total_value 
