#Write a function that reverses a string. The input string is given as an array
#of characters char[].
#
#Do not allocate extra space for another array, you must do this by modifying the
#input array in-place with O(1) extra memory.
#
#You may assume all the characters consist of printable ascii characters.
#
# 
#
#Example 1:
#
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]




class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #[r,a, t, s]
        #[s, r, a, t ,s ]

        start = 0
        end = len(s)-1

        while start < end:
            #actually reverse the elements
            temp = s[start]
            s[start] = s[end]
            s[end] = temp

            start = start + 1
            end = end - 1


        return s
        
