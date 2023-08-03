/**
 * @file 2210.숫자판점프.js
 * @author @apua34
 * @brief 
 * @link https://www.acmicpc.net/problem/2210
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

const inputArr = input.map((item) => item.split(' ').map(Number));

const answer = [];


function solution(x, y, str){
    const dir  = [
        [1, 0], 
        [-1, 0],
        [0, -1],
        [0, 1],
    ]

    if(str.length == 6){ // 문자열이 6자리가 되면 추가
        answer.push(str) // 1개씩
        return;
    }

    dir.forEach((target)=>{
        const [a, b] = target;

        // 상하좌우 이동이 가능한지,
        const top = x + a >= 0 
        const bottom = x + a < 5
        const left = y + b >= 0
        const right = y + b < 5

        if(top && bottom && left && right){
            const topBottm = x + a;
            const leftRight = y + b;
            const move = str + inputArr[x + a][y + b];
            solution(topBottm, leftRight, move);
        }
    })
}

for(let i = 0; i < 5; i++){
    for(let j = 0; j < 5; j++){
      solution(i, j , '') // START
    }
  }


console.log([...new Set(answer)].length)

