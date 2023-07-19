/**
 * @file 2225.합분해.js
 * @author @apua34
 * @brief 합분해
 * @version 0.1
 * @date 2023-07-17
 * @strategy 동적 계획법(Top-Down 방식)
 *
 * @copyright Copyright (c) 2023 @apua34
 *
 */

const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';

let input = fs.readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")


const numInput = input[0].split(" ").map(Number);

const [N, K] = numInput;
let dp = Array.from(new Array(N + 1), () => new Array(K + 1).fill(0));

function solution(N, K) {
    // ex) N = 4, K = 2
    if(N === 1) {
        dp[N][K] = K;
    }
    if(K === 1) {
        dp[N][K] = 1;
    }
    if(dp[N][K] === 0) {
        // 3, 2  + 4, 1
        dp[N][K] = solution(N - 1, K) + solution(N, K - 1);
    }

    return dp[N][K] % 1000000000; // 1000000000 나누는 이유는 단순 조건
}

const check = solution(N, K);
console.log(check);

// 참고링크 : https://mizzo-dev.tistory.com/entry/baekjoon2225 (해당 문제 복습 필요)
