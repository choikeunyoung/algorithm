const fs = require('fs')
const input = fs.readFileSync('./1526.txt').toString().trim()
const inputLength = input.length
const N = Number(input)

let ans = []
let max_value = 0

function backtracking(start) {
    if (start <= inputLength) {
        const answer = Number(ans.join(""))
        if (answer <= N) {
            if (max_value < answer) {
                max_value = answer
            }
        }
    } else {
        return
    }
    for (let i of ['4', '7']) {
        ans.push(i)
        backtracking(start + 1)
        ans.pop()
    }
}
backtracking(0)
console.log(max_value)