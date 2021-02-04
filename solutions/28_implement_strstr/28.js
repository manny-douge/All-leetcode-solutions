// Implement strStr().
// 
// Return the index of the first occurrence of needle in haystack, or -1 if needle
// is not part of haystack.
// 
// Clarification:
// 
// What should we return when needle is an empty string? This is a great question
// to ask during an interview.
// 
// For the purpose of this problem, we will return 0 when needle is an empty
// string. This is consistent to C's strstr() and Java's indexOf().
// 
//  
// 
// Example 1:
// 
// Input: haystack = "hello", needle = "ll"
// Output: 2

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if(needle.length == 0)
        return 0;

    //find needle string in haystack string
    //iterate over the haystack string
    for(let index = 0; index < haystack.length; index++) {
        if(haystack.substring(index, index + needle.length) == needle)
            return index;
    }
    return -1;
};
let haystack = "hello";
let needle = "ll";
let answer = 2;
console.log(`Input: Haystack: "${haystack}" Needle: "${needle}" Correct Answer: ${answer}`);
console.log(`My answer: ${strStr(haystack, needle)}`);
