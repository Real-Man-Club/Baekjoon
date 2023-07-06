/**
 * @file 9372.상근이의여행.js
 * @author @apua34
 * @brief 상근이의 여행
 * @version 0.1
 * @date 2023-07-07
 * @strategy MST(최소신장트리)
 *
 * @copyright Copyright (c) 2023 @apua34
 *
 */

const fs = require("fs");

// let input = fs.readFileSync("/dev/stdin")
//     .toString()
//     .trim()
//     .split("\n")
//     .map((v) => v.split(" ").map(Number));

let input = fs.readFileSync("input.txt")
    .toString()
    .trim()
    .split("\n")
    .map((v) => v.split(" ").map(Number));

const [limit, ...ary] = input;
let arr = ary.splice(0);

function solution(limit, travel) {
    let result = [];

    for (let i = 0; i < limit; i++) {
        const [N, M] = travel[0];
        travel.shift();

        for(let j = 0; j < M; j++) {
            travel.shift();
        };
        result.push(N - 1);
    };

    return result.join("\n");
}

const check = solution(limit, arr);
console.log(check);