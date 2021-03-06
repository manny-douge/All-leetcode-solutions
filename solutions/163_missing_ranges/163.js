//You are given an inclusive range [lower, upper] and a sorted unique integer
//array nums, where all elements are in the inclusive range.
//
//A number x is considered missing if x is in the range [lower, upper] and x is
//not in nums.
//
//Return the smallest sorted list of ranges that cover every missing number
//exactly. That is, no element of nums is in any of the ranges, and each missing
//number is in one of the ranges.
//
//Each range [a,b] in the list should be output as:
//
//"a->b" if a != b
//"a" if a == b
// 
//
//Example 1:
//
//Input: nums = [0,1,3,50,75], lower = 0, upper = 99
//Output: ["2","4->49","51->74","76->99"]
//Explanation: The ranges are:
//[2,2] --> "2"
//[4,49] --> "4->49"
//[51,74] --> "51->74"
//[76,99] --> "76->99"

var formatRange = function(lower, upper) {
    if(lower == upper)
        return `${upper}`;
    else
        return `${lower}->${upper}`;
}
var findMissingRanges = function(nums, lower, upper) {
    if(nums.length == 0)
        return [formatRange(lower, upper)];
    
    //ensure nums contains elements.
    //break down into 3 steps
    let missingRanges = [];
    
    //catch first edge case when first number isnt == lower
    if(nums[0] != lower)
        missingRanges.push(formatRange(lower, nums[0]-1));
    
    //handle missing ranges in between
    for(let i = 0; i < nums.length-1; i++) {
        if(nums[i+1]-nums[i] != 1)
            missingRanges.push(formatRange(nums[i]+1, nums[i+1]-1));
    }
    
    //catch second edge case when last number isnt == upper
    if(nums[nums.length-1] !=  upper)
        missingRanges.push(formatRange(nums[nums.length-1]+1, upper));
    
    return missingRanges;
};

let nums = [0, 1, 3, 50, 75];
let lower = 0;
let upper = 99;
let correct = ["2","4->49","51->74","76->99"]

console.log(`Input: [${nums}], Correct Answer = [${correct}]`);
console.log(`My answer: ${findMissingRanges(nums, lower, upper)}`);

