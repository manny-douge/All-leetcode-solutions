//Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
//Note: For the purpose of this problem, we define empty string as valid palindrome.
//
//Example 1:
//
//Input: "A man, a plan, a canal: Panama"
//Output: true
//Example 2:
//
//Input: "race a car"
//Output: false

/**
 * @param {string} s
 * @return {boolean}
 */

var isAlphaNumeric = function(s) {
    var re = /^[A-Za-z0-9]+$/
    if(s.match(re))
        return true;
    return false;
}
var isPalindrome = function(s) {
    if(s.length == 0)
        return true;

    let start = 0;
    let end = s.length-1;
    //reversal algorithm: 2 pointers
    //1 starts at the front, 1 starts at the end
    //decrement towards each other
    //iterate over string
    while(start < end) {
        //ensure that start poitner is alphanumeric
        while(start < end && !isAlphaNumeric(s[start]))
            start += 1;

        //ensure that end pointer is alphanumeric
        while(start < end && !isAlphaNumeric(s[end]))
            end -= 1;

        //if s[start].toLowerCase() != s[end].toLowerCase()
        if(s[start].toLowerCase() != s[end].toLowerCase())
            return false

        //increment start towards the end
        start += 1;
        //decrement end towards the begining
        end -= 1;
    }

    return true;

};

console.log(isPalindrome("meep | zooz peem"));
