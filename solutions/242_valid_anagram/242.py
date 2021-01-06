#Given two strings s and t , write a function to determine if t is an anagram of s.
#
#Example 1:
#
#Input: s = "anagram", t = "nagaram"
#Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        #dictionary letter -> occurences for word S
        l_dict = defaultdict(int)
        for letter in s:
            if letter in l_dict:
                l_dict[letter] = l_dict[letter] + 1
            else:
                l_dict[letter] = 1

        #iterate through second word
        for letter in t:
            if letter in l_dict:
                l_dict[letter] = l_dict[letter]-1
            else:
                return False

            if l_dict[letter] < 0:
                return False


        return True

