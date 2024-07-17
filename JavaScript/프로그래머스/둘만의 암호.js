function solution(s, skip, index) {
    let answer = '';
    let skipList = []
    for (change of skip) {
        skipList.push(change.charCodeAt())
    }

    for (word of s) {
        let asciiWord = word.charCodeAt()
        let cnt = 0
        while (cnt < index) {
            asciiWord += 1
            if (asciiWord > 122) {
                asciiWord = 97
            }
            if (skipList.includes(asciiWord)) {
                continue
            }
            else {
                cnt += 1
            }
        }
        answer += String.fromCharCode(asciiWord)
    }
    return answer
}