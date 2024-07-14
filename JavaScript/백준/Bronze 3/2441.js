const fs = require("fs");
const input = fs.readFileSync("./2441.txt").toString().trim();
const n = Number(input);

for (let i = 0; i < n; i++) {
    let ans = "";
    for (let j = 0; j < i; j++) {
        ans += " ";
    }
    for (let j = n - i; j > 0; j--) {
        ans += "*";
    }
    console.log(ans);
}