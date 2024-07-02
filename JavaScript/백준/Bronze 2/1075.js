const fs = require('fs')
const input = fs.readFileSync('./1075.txt').toString().trim().split("\n")

N = parseInt(input[0])
F = parseInt(input[1])
if (N % F === 0) {
    console.log(input[0].slice(-3, -1))
} else {
    let newInput = Number(Math.floor(N / 100) + "00")
    for (let i = 0; i <= 100; i++) {
        const checkInput = newInput + i
        if (checkInput % F == 0) {
            const strCheck = String(checkInput)
            console.log(strCheck.slice(-2, strCheck.length))
            break
        }
    }
}