#Given a non-negative integer numRows, generate the first numRows of Pascal's
#triangle.
#
#
#In Pascal's triangle, each number is the sum of the two numbers directly above
#it.
#
#Example:
#
#Input: 5
#Output:
ans = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

class Solution:
    def generate(self, numRows: int):
        
        triangle = []
        for row_num in range(1, numRows+1):
            row_list = [0] * row_num
            row_list[0] = 1
            row_list[row_num-1] = 1
            for index in range(1, row_num-1):
                row_list[index] = triangle[row_num-2][index] + triangle[row_num-2][index-1]
            triangle.append(row_list)
        
        return triangle


print(ans)
print(Solution().generate(5))
