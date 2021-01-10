#387. First Unique Character in a String Given a string, find the first
#non-repeating character in it and return its index. If it doesn't exist, return
#-1.
#
#Examples:
#
#s = "leetcode"
#return 0.
#

#
#
#Note: You may assume the string contains only lowercase English letters.

s = "loveleetcode"
ans = 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l_dict = {}
        
        for letter in s:
            if letter in l_dict:
                l_dict[letter] = l_dict[letter]+1
            else:
                l_dict[letter] = 1
        
        for index in range(len(s)):
            if l_dict[s[index]] == 1:
                return index
        
        return -1

print(f"Input: {s}")
print(f" ans = {ans}, sol = {Solution().firstUniqChar(s)}")
