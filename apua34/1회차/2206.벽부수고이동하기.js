/**
 * @file 2206.벽부수고이동하기.js
 * @author @apua34
 * @brief 벽부수고 이동하기
 * @version 0.1
 * @date 2023-07-17
 * @strategy BFS(너비 우선 탐색 - Queue)
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

let [N, M] = input[0].split(" ").map(Number);

input = input.slice(1).map((v) => v.split("").map(Number));
const ch = Array.from(new Array(N), () => new Array());

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const queue = [];

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
    ch[i][j] = new Array(2).fill(0);
    }
}

ch[0][0][0] = 1;
queue.push([0, 0, 0]);

function BFS(N, M) {
    let idx = 0;

    while (idx !== queue.length) {
    const [y, x, isBreak] = queue[idx];

    if (x === M - 1 && y === N - 1) {
        return ch[y][x][isBreak];
    }

    for (let i = 0; i < dx.length; i++) {
        const [nx, ny] = [x + dx[i], y + dy[i]];

        if (nx >= 0 && nx < M && ny >= 0 && ny < N) {

                if (input[ny][nx] === 0 && ch[ny][nx][isBreak] === 0) {
                    ch[ny][nx][isBreak] = ch[y][x][isBreak] + 1;
                    queue.push([ny, nx, isBreak]);
                } 
                if (input[ny][nx] === 1 && isBreak === 0) {
                    ch[ny][nx][isBreak + 1] = ch[y][x][isBreak] + 1;
                    queue.push([ny, nx, isBreak + 1]);
                }
            }
        }
        idx++;
    }
    return -1;
}

const check = BFS(N, M);
console.log(check);

// 참고링크 : https://velog.io/@arthur/2206.-%EB%B2%BD-%EB%B6%80%EC%88%98%EA%B3%A0-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-node.js-javascript (다시 풀것)
