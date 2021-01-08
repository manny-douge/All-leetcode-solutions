#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
#M.
#
#Symbol       Value I             1 V             5 X             10 L
#50 C             100 D             500 M             1000 For example, 2 is
#written as II in Roman numeral, just two one's added together. 12 is written as
#XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V
#+ II.
#
#Roman numerals are usually written largest to smallest from left to right.
#However, the numeral for four is not IIII. Instead, the number four is written
#as IV. Because the one is before the five we subtract it making four. The same
#principle applies to the number nine, which is written as IX. There are six
#instances where subtraction is used:
#
#I can be placed before V (5) and X (10) to make 4 and 9.  X can be placed before
#L (50) and C (100) to make 40 and 90.  C can be placed before D (500) and M
#(1000) to make 400 and 900.  Given a roman numeral, convert it to an integer.
#
# 
#
#Example 1:
#
#Input: s = "III"
#Output: 3
#Example 2:
#
#Input: s = "IV"
#Output: 4
#Example 3:
#
#Input: s = "IX"
#Output: 9

class Solution:
    def romanToInt(self, s: str) -> int:
        double_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        symbol_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }


        if len(s) == 1:
            return symbol_dict[s]

        letter_index = 0
        total = 0
        while letter_index < len(s)-1:
            double_roman = s[letter_index] + s[letter_index+1]
            if double_roman in double_dict:
                total += double_dict[double_roman]
                letter_index += 2
            else:
                total += symbol_dict[s[letter_index]]
                letter_index += 1

        if letter_index != len(s):
            total += symbol_dict[s[letter_index]]


        return total


