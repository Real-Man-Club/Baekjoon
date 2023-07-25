/**
 * @file 2302.극장좌석.js
 * @author @apua34
 * @brief 
 * @link https://www.acmicpc.net/problem/2302
 * @version 0.1
 * @date 2023-07-23
 * @strategy DP
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

const [N, M, ...arr] = input;


function solution(N, M, arr) {
    const n = Number(N);
    const m = Number(M);

    if(n === m) return 1;

    let result = [];

    const vip = Array(n + 1).fill(false); // visited
    arr.map((target) => vip[target] = true);
    
    const fibo_memo = [0, 1, 2];
    
    for (let i = 3; i <= N - M; i++) {
        fibo_memo[i] = fibo_memo[i - 1] + fibo_memo[i - 2];
    }

    let current = 0;
    let value = 1;

    for(let i = 1; i <= N; i++) {

        if(!vip[i]) {
            value = fibo_memo[++current];
        } 
        
        if(vip[i]) {
            result.push(value);
            current = 0;
            value = 1;
        }
    }

    result.push(value);

   return result.reduce((acc, value) => acc * value, 1)
}

const check = solution(N, M, arr);
console.log(check)

