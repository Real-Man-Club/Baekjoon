/**
 * @file 2002.추월.js
 * @author @apua34
 * @brief 추월
 * @link https://www.acmicpc.net/problem/2002
 * @version 0.1
 * @date 2023-07-20
 * @strategy 맵, 해쉬
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

const inputTunnelCar = arr.slice(0, N);
const outputTunnelCar = arr.slice(N);

const inputTunnelCarMap = new Map();

// 터널로 진입한 자동차
inputTunnelCar.forEach((element, idx) => {
    inputTunnelCarMap.set(element, idx)
})

const visited = Array.from({ length: N }, () => false);

function solution(inputTunnelCarMap, outputTunnelCar, visited) {
  let cur = 0;
  let answer = 0;
  let flag = false;
  
  // 터널에서 나온 자동차
  outputTunnelCar.forEach((element) => {
      if (inputTunnelCarMap.get(element) > cur) {
        for (let i = 0; i < inputTunnelCarMap.get(element); i++) {
          // 추월한 경우
          if (!visited[i]) {
            flag = true;
            answer++;
            break;
          }
        }
        if (!flag) {
          cur = inputTunnelCarMap.get(element) + 1;
        }
      }
      visited[inputTunnelCarMap.get(element)] = true;
  })

  return answer;
}

const check = solution(inputTunnelCarMap, outputTunnelCar, visited);
console.log(check);


