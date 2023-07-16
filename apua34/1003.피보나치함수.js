const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';

let input = fs.readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")
    
input.shift() // 맨 앞에값 제거

for (let i of input) {
    const fibonacci = [[1, 0], [0, 1]];
    // 0, 1에 대한 idx는 고정
    for (let j = 2; j <= i; j++) {
        fibonacci[j] = [
            fibonacci[j - 1][0] + fibonacci[j - 2][0],
            fibonacci[j - 1][1] + fibonacci[j - 2][1]
        ];
    }
    console.log(fibonacci[i])
}

