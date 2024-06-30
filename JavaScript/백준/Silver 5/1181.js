const fs = require("fs");
let input = fs.readFileSync("./1181.txt").toString().trim().split("\n");

N = input.splice(0, 1);
answer = [];

input.sort((a, b) => {
  if (a.length > b.length) return 1;
  else if (a.length < b.length) return -1;
  else return a > b ? 1 : -1;
});

input.forEach((word) => {
  if (!answer.includes(word)) {
    answer.push(word);
  }
});

for (word of answer) {
  console.log(word);
}
