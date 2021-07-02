// 2 pointer with sort
class TwoSum {
  arr: number[];
  lastSortLength: number;

  constructor() {
    this.arr = [];
    this.lastSortLength = 0;
  }

  add(number: number): void {
    this.arr.push(number);
  }

  find(value: number): boolean {
    if(this.lastSortLength !== this.arr.length) {
      this.arr.sort((a,b) => a-b); // N LogN time worst case
    }  
    
    // Use 2 pointer method to find if two values add up
    
    let low = 0;
    let high = this.arr.length-1;
    while (low < high) {
      if (this.arr[low] + this.arr[high] < value) {
        low += 1;
      } else if (this.arr[low] + this.arr[high] > value) {
        high -= 1;
      } else if (this.arr[low] + this.arr[high] === value) {
        return true;
      } 
    }
    return false;
  }
}



const nums = [1, 3, 5, 4, 7];
const sumToFind = 8;
const twoSum = new TwoSum();
for (const num of nums) {
  twoSum.add(num); 
}
console.log(`Adding nums: ${nums}`);
console.log(`Sum for ${sumToFind} exists: ${twoSum.find(sumToFind)}`);
