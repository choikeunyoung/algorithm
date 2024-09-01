function solution(x, y, n) {
    let answer = 0;
    let targetCnt = 10 ** 9
    let queue = [[y, 0]]
    let visited = []
    for (let i = 0; i <= y; i++) {
        visited.push(false)
    }
    if (x === y) {
        targetCnt = 0
    } else {
        while (queue.length > 0) {
            const next = queue.shift()
            const doubleNext = Number(next[0] / 2)
            const threeNext = Number(next[0] / 3)
            const addNext = next[0] - n
            const nextCnt = next[1] + 1
            if (targetCnt <= nextCnt) {
                break
            }
            if (doubleNext >= x) {
                if (doubleNext === x) {
                    targetCnt > nextCnt ? targetCnt = nextCnt : targetCnt = targetCnt
                }
                if (visited[doubleNext] === false) {
                    visited[doubleNext] = true
                    queue.push([doubleNext, nextCnt])
                }
            }

            if (threeNext >= x) {
                if (threeNext === x) {
                    targetCnt > nextCnt ? targetCnt = nextCnt : targetCnt = targetCnt
                }
                if (visited[threeNext] === false) {
                    visited[threeNext] = true
                    queue.push([threeNext, nextCnt])
                }
            }

            if (addNext >= x) {
                if (addNext === x) {
                    targetCnt > nextCnt ? targetCnt = nextCnt : targetCnt = targetCnt
                }
                if (visited[addNext] === false) {
                    visited[addNext] = true
                    queue.push([addNext, nextCnt])
                }
            }
        }
    }

    if (targetCnt !== 10 ** 9) {
        answer = targetCnt
    } else {
        answer = -1
    }
    return answer;
}

