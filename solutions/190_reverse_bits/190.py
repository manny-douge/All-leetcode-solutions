#Reverse bits of a given 32 bits unsigned integer.
n = 43261596
correct = 964176192

class Solution:
    def reverseBits(self, n):

    #   0,1,1,0 >> 1 = 0,0,1,1
    #   0,1,1,0 << 1 = 1,1,0,0

    #   input: 1100 last:0  output:

    #14 -> 0111  n & 1  output: 0 << 1 = 01 = 1110
        output = 0
        for _ in range(32):

            output = output << 1

            if n & 1:
                output += 1

            n = n >> 1


        return output

print(f"Input: {n}, Correct: {correct}")
print(f"My answer: {Solution().reverseBits(n)}")
