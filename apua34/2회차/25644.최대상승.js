/**
 * @file 25644.최대상승.js
 * @author @apua34
 * @brief 최대 상승
 * @link https://www.acmicpc.net/problem/25644
 * @version 0.1
 * @date 2023-07-19
 * @strategy 그리디
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
let numberArr = arr.map((item) => item.split(" ").map(Number))[0];

function solution(N, arr) {
    let answer = 0;
    let elementStock = 0;

    // ex) N = 5, 뒤에서 부터 진행
    for(let i = N - 1; i >= 0; i--) { 
        elementStock = Math.max(elementStock, arr[i]); // 0, 5
        answer = Math.max(answer, elementStock - arr[i]);  // 주가 공식 : 0 - 5
    }
    
    return answer;
}

const check = solution(N, numberArr);
console.log(check);


