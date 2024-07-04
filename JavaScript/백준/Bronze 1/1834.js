const fs = require('fs')
const input = BigInt(fs.readFileSync('./1834.txt').toString().trim())

let total = String((input + 1n) * input / 2n * (input - 1n))
console.log(total)