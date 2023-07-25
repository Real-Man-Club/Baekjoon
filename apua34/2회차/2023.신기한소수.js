/**
 * @file 2023.신기한소수.js
 * @author @apua34
 * @brief 신기한 소수
 * @link https://www.acmicpc.net/problem/2023
 * @version 0.1
 * @date 2023-07-23
 * @strategy 백트래킹, 재귀
 *
 * @copyright Copyright (c) 2023 @apua34
 *
 */

// node.js 메모리 초과 : https://www.acmicpc.net/board/view/79930

const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath)
    .toString()
    .trim()

const N = Number(input);

// 소수 구하기
function isPrime(num){
  if(num === 0 || num === 1) return false;
  
  for(let i = 2; i < num; i++){
    if(num % i === 0) return false;      
  }

  return true;   
}

function dfs(num, input) {
  if(input === 0) {
    console.log(num); // 종료
  }

  for(let i = 1; i < 10; i++) {
    let tmp = (10 * num) + i;

    if(input > 0 && isPrime(tmp)) {
      dfs(tmp, input - 1);
    }
  }
}

dfs(0, N); // 시작

