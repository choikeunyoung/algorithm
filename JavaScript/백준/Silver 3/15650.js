const fs = require("fs");
const input = fs.readFileSync("./15650.txt").toString().trim().split(" ");

N = Number(input[0]);
M = Number(input[1]);

let answerList = [];

function backtracking(start, level) {
  if (level === M) {
    console.log(...answerList);
    return;
  }
  for (let i = start; i <= N; i++) {
    answerList.push(i);
    backtracking(i + 1, level + 1);
    answerList.pop();
  }
}

backtracking(1, 0);
