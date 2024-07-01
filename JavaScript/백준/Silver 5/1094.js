// 인풋
const fs = require("fs");
const input = parseInt(fs.readFileSync("./1094.txt").toString().trim());
// 막대길이 64
let bar = 64;
// 자른 막대 저장 리스트
let barList = [];
// 총 길이 체크
let total = 0;
// 몇개 사용했는지 체크
let count = 0;
if (input === bar) {
  // 막대가 64이고 X값이 64인 경우 1개의 막대만 사용
  console.log(count + 1);
} else {
  // 외의 경우 막대가 1이 나올때 까지 분리
  while (bar > 1) {
    // check 변수를 통해서 X 보다 작은 막대를 다 저장
    const check = bar / 2;
    if (check <= input) {
      barList.push(check);
    }
    bar /= 2;
  }
  //   저장된 막대를 더하고 빼면서 몇개를 사용했는지 체크
  for (bar of barList) {
    total += bar;
    count += 1;
    if (total > input) {
      total -= bar;
      count -= 1;
    } else if (total == input) {
      console.log(count);
      break;
    }
  }
}
