const fs = require("fs");
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';

let input = fs.readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")

const [inputs, ...arr] = input;
let numberArr = [];

arr.map(item => {
    numberArr.push(item.split(' ').map(Number));
});

function rotate(N, M, currentArr) {

    const currentCount = Math.min(N, M) / 2;
    let rotationalArr = currentArr;
  
    for(let rotation = 0; rotation < currentCount; rotation++) {
        const row = N - rotation - 1;
        const col = M - rotation - 1;
        const tmp = rotationalArr[rotation][rotation];
    
        // TOP
        for(let j = rotation; j < col; j++) {
            rotationalArr[rotation][j] = rotationalArr[rotation][j + 1];
        }
        // RIGHT
        for(let i = rotation; i < row; i++) {
            rotationalArr[i][col] = rotationalArr[i + 1][col];
        }
        // BOTTOM
        for(let j = col; j > rotation; j--) {
            rotationalArr[row][j] = rotationalArr[row][j - 1];
        }
        // LEFT
        for(let i = row; i > rotation; i--) {
            rotationalArr[i][rotation] = rotationalArr[i - 1][rotation];
        }

        rotationalArr[rotation + 1][rotation] = tmp;
    }

    return rotationalArr;
}

function solution(inputs, arr) {
    // N : x축, M : y축, R : 회전수
    const [N, M, R] = inputs.split(' ').map(Number);
    let result = arr;
    
    for(let i = 0; i < R; i++) {
        result = rotate(N, M, result);
    }

    return result.map(row => {
        console.log(row.join(' '));
    });
}

solution(inputs, numberArr);