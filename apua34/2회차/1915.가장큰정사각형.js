/**
 * @file 1915.가장큰정사각형.js
 * @author @apua34
 * @brief 
 * @link https://www.acmicpc.net/problem/1915
 * @version 0.1
 * @date 2023-07-23
 * @strategy DFS
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

const [N, M] = input.shift().split(' ').map(Number); // 4, 4

let arr = Array.from({ length: N }, () => Array.from({ length: M }, () => 0));
input.map((item, idx) => (arr[idx] = item.trim().split('').map(Number)));
let dp = arr.map((item) => [...item]);


function solution(N, M, arr) {
    let answer = 0;

    for (let i = 1; i < N; i++) {
        for (let j = 1; j < M; j++) {
            if (arr[i][j]) { // 0이 아니라면

                let left = dp[i - 1][j - 1]; 
                let leftTop = dp[i - 1][j];
                let top = dp[i][j - 1];

                dp[i][j] = Math.min(left, leftTop, top) + 1;
            };
        }
    }

    // 제일 큰 수 넣어주기
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if(dp[i][j] > answer) {
                answer = dp[i][j];
            }
        }
    }

    return answer * answer; 
}

const check = solution(N, M, arr)
console.log(check);

