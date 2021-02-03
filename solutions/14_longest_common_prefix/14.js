//Write a function to find the longest common prefix string amongst an array of strings.
//
//If there is no common prefix, return an empty string "".
//
// 
//
//Example 1:
//
//Input: strs = ["flower","flow","flight"]
//Output: "fl"
//Example 2:
//
//Input: strs = ["dog","racecar","car"]
//Output: ""
//Explanation: There is no common prefix among the input strings

/**
 * @param {string[]} strs
 * @return {string}
 */

var longestCommonPrefix = function(strs) {
    if(strs.length == 0) {
        return "";
    }

    let first_str = strs[0];
    let end = strs.length;
    let i = 1;
    
    //we can start with the first string
    //while i < strs.length
    for(let i = 0; i < strs.length; i++) {
        //while first_str isnt empty && first_str isnt in the current string
        while(first_str.length != 0 && !(first_str == strs[i].substr(0, first_str.length)))
            //remove last character in first string
            first_str = first_str.substring(0, first_str.length-1);
        
        if(first_str.length == 0)
            return "";
    }
    //if we make it out here
    return first_str;
}

let input = ["flower","flow","flight"]
let answer = "fl";

console.log(`Input: [${input}] Answer:${answer}`);
console.log(`My answer: ${longestCommonPrefix(input)}`);
