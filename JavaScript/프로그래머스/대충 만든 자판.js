function solution(keymap, targets) {
    let answer = []
    for (target of targets) {
        let total = 0
        for (tar of target) {
            let minValue = 10 ** 9
            for (key of keymap) {
                const value = key.indexOf(tar)
                if (value < minValue && value !== -1) {
                    minValue = value + 1
                }
            }
            total += minValue
        }
        if (total >= 10 ** 9) {
            total = -1
        }
        answer.push(total)
    }
    return answer;
}