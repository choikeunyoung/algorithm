function solution(n, m, section) {
    let answer = 0;
    let paintList = [0]
    let sectionLength = section.length
    for (let i = 0; i < n; i++) {
        paintList.push(0)
    }
    let cnt = 1
    for (let i = 0; i < sectionLength; i++) {
        const current = section[i]
        let flag = 0
        if (i === sectionLength - 1) {
            if (paintList[current] === 0) {
                paintList[current] = cnt
                cnt += 1
            }
        } else {
            if (paintList[current] === 0) {
                for (let j = 0; j < m; j++) {
                    const tail = current + j
                    if (tail < n + 1) {
                        if (paintList[tail] === 0) {
                            paintList[tail] = cnt
                            flag = 1
                        }
                    } else {
                        break
                    }
                }
                if (flag === 1) {
                    cnt += 1
                }
            }
        }
    }
    answer = cnt - 1
    return answer;
}