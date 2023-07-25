/**
 * @file 10973.이전순열.js
 * @author @apua34
 * @brief 이전 순열
 * @link https://www.acmicpc.net/problem/10973
 * @version 0.1
 * @date 2023-07-20
 * @strategy 구현
 *
 * @copyright Copyright (c) 2023 @apua34
 *
 */

const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")

const [N, ...arr] = input;

let numbers = [];

for (let i = 1; i <= N; i++) {
  numbers.push(i)
}

let next = arr.split(" ").map((i) => Number(i));
let sortNumbers = [...numbers].sort((a, b) => a - b);

function solution() {
    if (next.every((num, index) => num === sortNumbers[index])){
        return -1
    }
    
    let i = N - 2;
    while (next[i] < next[i + 1]) i--;

    let j = N - 1; 
    while (next[i] < next[j]) j--;

    [next[i], next[j]] = [next[j], next[i]];
   
    let rest = next.slice(i + 1);
    rest.sort((a, b) => b - a); 

    let answer = [...next.slice(0, i + 1), ...rest]; 
  
  return answer.join(" ");
}

const check = solution();
console.log(check);


