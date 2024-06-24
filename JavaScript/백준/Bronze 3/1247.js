const fs = require("fs")
const input = fs.readFileSync("./1247.txt").toString().trim().split("\n")
let start = 0
for (i in input) {
    let total = 0
    for (let j = start; j < i + start; j++) {
        total += input[j]
    }
    if (total < 0) {
        console.log("-")
    } else if (total > 0) {
        console.log("+")
    } else {
        console.log(0)
    }
    start += i
}