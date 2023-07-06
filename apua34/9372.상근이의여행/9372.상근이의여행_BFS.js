/**
 * @file 9372.상근이의여행.js
 * @author @apua34
 * @brief 상근이의 여행
 * @version 0.1
 * @date 2023-07-07
 * @strategy BFS(너비우선탐색)
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

let input = fs.readFileSync("../input.txt")
    .toString()
    .trim()
    .split("\n")
    .map((v) => v.split(" ").map(Number));

const [limit, ...ary] = input;

function solution(limit, travel) {
    let result = [];
    let idx = 1;

    for (let i = 0; i < limit; i++) {
        let arr = [];
        let [N, M] = travel[idx++];

        for (let j = 0; j < M; j++) {
            arr[j] = travel[idx++];
        }
    
        const visited = new Array(N).fill(false);
        visited[0] = true;
        const queue = [0];
        let count = 0;
    
        while (queue.length) {
            const head = queue.shift();

            for (let node of arr) {
                if (node[0] - 1 === head && !visited[node[1] - 1]) {
                    queue.push(node[1] - 1);
                    visited[node[1] - 1] = true;
                    count++;
                } 
                 if (node[1] - 1 === head && !visited[node[0] - 1]) {
                    queue.push(node[0] - 1);
                    visited[node[0] - 1] = true;
                    count++;
                }
            }
            if (!visited.includes(false)) break;
        }
        result[i] = count;
    }
    return result.join('\n');
}

const check = solution(limit, ary);
console.log(check)