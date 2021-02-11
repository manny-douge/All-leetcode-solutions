//Given a signed 32-bit integer x, return x with its digits reversed. If reversing
//X causes the value to go outside the signed 32-bit integer range [-231, 231 -
//1], then return 0.
//
//Assume the environment does not allow you to store 64-bit integers (signed or
//Unsigned).
//
// 
//
//Example 1:
//
//Input: x = 123
//Output: 321
//Example 2:
//
//Input: x = -123
//Output: -321
//Example 3:
var reverse = function(x) {
    if(x.toString().length == 1)
        return x;
    
    let x_str = x.toString();
    let x_rev = "";
    //turn x -> string
    let end = x_str.length-1;
    //iterate over string in reverse
    while(end >= 0) {
        x_rev += x_str[end];
        end -= 1;
    }
    
    //iterate over string //ignoring - signs and removing zeros until we find our first none zero number
    while(x_rev.length != 0 && x_rev[0] == '0') {
        if(x_rev[0] == '0')
            x_rev = x_rev.substring(1, x_rev.length);
        //else if zero
            //remove. zero from string
    }
        
    let rev_int = parseInt(x_rev);
    rev_int = (x < 0) ? -rev_int : rev_int;
    //cast string to integer
    if(rev_int > (2 ** 31)-1 || rev_int < -(2 ** 31))
        return 0;

    return rev_int;
};

let x = 901000;
let answer = 109;

console.log(`Input: ${x}, Correct answer: ${answer}`);
console.log(`My answer: ${reverse(x)}`);
