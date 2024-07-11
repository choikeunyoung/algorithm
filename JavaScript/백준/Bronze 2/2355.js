const fs = require('fs')
const input = fs.readFileSync('./2355.txt').toString().trim().split(" ")

A = parseInt(input)
B = parseInt(input)

A > B ? console.log((A + B) * (A - B + 1) / 2) : console.log((A + B) * (B - A + 1) / 2)