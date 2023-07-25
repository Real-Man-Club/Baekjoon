/**
 * @file 15989.1,2,3더하기4.js
 * @author @apua34
 * @brief 1, 2, 3 더하기 4
 * @link https://www.acmicpc.net/problem/15989
 * @version 0.1
 * @date 2023-07-21
 * @strategy 디아나믹 프로그래밍
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
const numberArr = arr.map(Number);

function solution(N, arr) {
    let answer = [];
    let dp = [];

    dp[0] = 1; // 1 - 1가지
    dp[1] = 2; // 2 : 1, 1 + 1 - 2가지
    dp[2] = 3; // 3 : 1 + 1 + 1, 1 + 2, ...

    for (let i = N - 1; i <= N; i++) {
        for (let j = i; j <= 10001; j++) { // n은 양수이며 10,000보다 작다.
             dp[j] = dp[i] + dp[i - 1];
        }
    }
      
    arr.forEach(item => {
        answer.push(dp[item]);
    })

    return answer;
}

const printing = solution(N, numberArr);

// Print
printing.forEach((item) => {
    console.log(item)
})

