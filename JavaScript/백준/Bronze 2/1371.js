const fs = require('fs')
let input = fs.readFileSync('./1371.txt').toString().replace(/\n|\r/g, "").split(" ")

let wordObject = Object()
let maxValue = 0
for (words of input) {
    for (word of words) {
        if (wordObject[word]) {
            wordObject[word] += 1
        } else {
            wordObject[word] = 1
        }
        if (wordObject[word] > maxValue) {
            maxValue = wordObject[word]
        }
    }
}

const wordArray = []

for (const [key, value] of Object.entries(wordObject)) {
    if (value == maxValue) {
        wordArray.push(key)
    }
}

const answer = wordArray.sort()
console.log(answer.join(""))