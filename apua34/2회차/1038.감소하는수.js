/**
 * @file 1038.감소하는수.js
 * @author @apua34
 * @brief 
 * @link https://www.acmicpc.net/problem/1038
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

const N = Number(input[0]);

function solution(N) {

    // 이 문제의 입력 최대치는 1,000,000 이지만, 실제로 사용될 수 있는 입력의 수는 1023개이다.

    // 그 이유는 이 문제가 10진수의 감소하는 수이기 때문이다. 10진수에서는 총 10가지의 수만을 이용할 수 있기에, 
    // 이 상황에서 나올 수 있는 최대값은 '9876543210'이다. 
    // 이는 총 10자리수이며 첫번째 자리에서 나올수 있는 경우의수는 9로 한가지만 존재한다. 
    // 왜냐하면 10진수에서 첫번째 자리 수에 9이외에 다른 숫자가 오는 감소하는 수는 존재하지 않기 때문. 

    // 같은 이유로 두번째 자리에는 2가지의 숫자만 올 수 있고, 세번째 자리에는 3가지의 숫자만 올 수 있다. 
    // 이를 바탕으로 이 문제에서 발생할 수 있는 감소하는 수는 총 1023개인것을 알 수 있다.
    // (10C1 + 10C2 ... 10C10 = 2^10 또는 원소가 10개인 집합의 부분집합의 갯수)

    if(N > 1022) return -1;

    let result = [];

    for(let i = 1; i <= 1023; i++){
        let num = 0;
        let tmp = i;

        for(let idx = 9; idx >= 0; idx--){
            if(tmp % 2 == 1){
                num = (10 * num) + idx;
            }
            tmp = Math.floor(tmp / 2);
        }
        result.push(num);
    }
    
    result.sort((a,b) => a - b);

    return result[N];
}

const check = solution(N);
console.log(check);


