var isValid = function(s) {
    //we need a dictionary to map opening -> closing brackets
    let mapping = {
        "(": ")",
        "{": "}",
        "[": "]",
    };
    
    //we need a stack to enforce order for the rules
    let stack = [];
    
    //iterate through the string
    for(let chr of s) {
        //if is a opening bracket
        if(chr in mapping) {
            //add it to the stack
            stack.push(chr);
        } else if (stack.length != 0 && mapping[stack[stack.length-1]] == chr) {
        //else if this symbol matches the top of the stacks closing bracket
            stack.pop();
        } else {
            return false;
        }
    }
    
    return stack.length == 0;
    
};
let input = "()[]{}";
let correct = true;
console.log(`Input: "${input}", Correct: ${correct}`);
console.log(`My answer: :${isValid(input)}`);
