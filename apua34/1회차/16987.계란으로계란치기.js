/**
 * @file 16987.계란으로계란치기.js
 * @author @apua34
 * @brief 계란으로 계란치기
 * @version 0.1
 * @date 2023-07-16
 * @strategy DFS(깊이 우선 탐색 - 재귀)
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

const [N, ...arr] = input;

let eggs = [];
let answer = 0;

arr.map(item => {
    eggs.push(item.split(' ').map(Number));
});


function dfs(recent, N, eggs) {
    if (recent == N) {
        let broken = 0;

        for (let i = 0; i < N; i++) {
            if (eggs[i][0] <= 0) broken++;
        }

        answer =  Math.max(broken, answer);

        return ;
    }

    let flag = true;

    for (let next = 0; next < N; next++) {
        if (next == recent) continue;
        if (eggs[recent][0] <= 0 || eggs[next][0] <= 0) continue;

        flag = false;

        eggs[recent][0] = eggs[recent][0] - eggs[next][1];
        eggs[next][0] = eggs[next][0] - eggs[recent][1];

        dfs(recent + 1, N, eggs);

        eggs[recent][0] = eggs[recent][0] + eggs[next][1];
        eggs[next][0] = eggs[next][0] + eggs[recent][1];
    }

    if (flag) dfs(recent + 1, N, eggs)
}

dfs(0, N, eggs);

console.log(answer)

// 참고 링크 : https://velog.io/@adorno10/%EA%B9%8A%EC%9D%B4-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89-Depth-first-search-DFS
