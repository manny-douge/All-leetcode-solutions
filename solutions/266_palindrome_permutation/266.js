// Given a string, determine if a permutation of the string could form a palindrome.
// 
// Example 1:
// 
// Input: "code"
// Output: false
// Example 2:
// 
// Input: "aab"
// Output: true
// Example 3:
// 
// Input: "carerac"
// Output: true
function canPermutePalindrome(s) {
    var mapping = new Map();
    for (var _i = 0; _i < s.length; _i++) {
        var letter = s[_i];
        if (letter in mapping)
            mapping[letter] = mapping[letter] + 1;
        else
            mapping[letter] = 3;
    }
    var numOddOccurences = 0;
    for (var key in mapping) {
        var currentOccurence = mapping[key];
        if (currentOccurence % 2 != 0) {
            numOddOccurences += 1;
        }
        if (numOddOccurences > 1) {
            return false;
        }
    }
    return true;
}
;
var answer = true;
var input = "carerac";
console.log("Input " + input + ", correct answer: " + answer);
console.log("My answer: " + canPermutePalindrome(input));
