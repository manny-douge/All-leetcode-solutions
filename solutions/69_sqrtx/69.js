//Given a non-negative integer x, compute and return the square root of x.
//
//Since the return type is an integer, the decimal digits are truncated, and only
//the integer part of the result is returned.
//
// 
//
//Example 1:
//
//Input: x = 4
//Output: 2
//Example 2:
//
//Input: x = 8
//Output: 2
//Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    
    if(x <= 1)
        return x;
    
    let low = 1;
    let high = x;
    
    while(low < high) {
        let mid = low + Math.floor((high-low)/2);
        if(mid ** 2 == x) {
            return mid;
        } else if(mid ** 2 > x) {
            high = mid;
        } else if(mid ** 2 < x) {
            low = mid + 1
        }
    }
    
    return low-1;
};
let input = 8;
let answer = 2;
console.log(`Input: ${input} Correct Answer: ${answer}`);
console.log(`My answer: ${mySqrt(input)}`);
