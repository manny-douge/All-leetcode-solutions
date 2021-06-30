/**
 * Definition for read4()
 * read4 = function(buf4: string[]): number {
 *     ...
 * };
 */

var solution = function(read4: any) {
  return function(buf: string[], n: number): number {
    let buf4 = new Array(4); 
    // Convenient to set readChars to 4 so we can use !== 4 as end point.
    let readChars = 4;
    let copiedChars = 0;
    while(copiedChars < n && readChars === 4) {
      readChars = read4(buf4);
      
      // Try to copy all the read characters into the internal buffer.j
      for (let i = 0; i < readChars; i++) {
        buf[copiedChars] = buf4[i]; 
        copiedChars += 1;
        
        // If we ever reach n copied characters, then stop.
        if (copiedChars === n) return copiedChars;
      }
    }
    return copiedChars;
  };
};
