// 2 pointer with sort
var TwoSum = /** @class */ (function () {
    function TwoSum() {
        this.arr = [];
        this.lastSortLength = 0;
    }
    TwoSum.prototype.add = function (number) {
        this.arr.push(number);
    };
    TwoSum.prototype.find = function (value) {
        if (this.lastSortLength !== this.arr.length) {
            this.arr.sort(function (a, b) { return a - b; }); // N LogN time worst case
        }
        // Use 2 pointer method to find if two values add up
        var low = 0;
        var high = this.arr.length - 1;
        while (low < high) {
            if (this.arr[low] + this.arr[high] < value) {
                low += 1;
            }
            else if (this.arr[low] + this.arr[high] > value) {
                high -= 1;
            }
            else if (this.arr[low] + this.arr[high] === value) {
                return true;
            }
        }
        return false;
    };
    return TwoSum;
}());
var nums = [1, 3, 5, 4, 7];
var sumToFind = 8;
var twoSum = new TwoSum();
for (var _i = 0, nums_1 = nums; _i < nums_1.length; _i++) {
    var num = nums_1[_i];
    twoSum.add(num);
}
console.log("Adding nums: " + nums);
console.log("Sum for " + sumToFind + " exists: " + twoSum.find(sumToFind));
