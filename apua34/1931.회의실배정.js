const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';

let input = fs.readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")

const [limit, ...ary] = input; 
let schedules = [];

for(let i of ary) {
    let item = i.split(" ");
    schedules.push([Number(item[0]), Number(item[1])]);
}

// End 포인트가 같을 경우 (ex. [4, 5], [3, 5]) Start 포인트를 기준으로 정렬
// 2차원 Sort : https://ywtechit.tistory.com/269

schedules = schedules.sort((a, b) => {
    return a[1] === b[1] ? a[0] - b[0] : a[1] - b[1];
})

function solution(limit, ary) {

    let point = 0;
    let result = 0;

    for(let i = 0; i < limit; i++) {
        const [start, end] = ary[i];
        if(point <= start) {
            point = end;
            result++;
        }
    }

    console.log(result) // 이거 안쓰면 틀렸다고..?
    return result;
}

solution(limit, schedules);