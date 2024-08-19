function solution(s) {
    let answer = [];
    let wordDict = {}
    for (index in s) {
        if (!(s[index] in wordDict)) {
            wordDict[s[index]] = Number(index)
            answer.push(-1)
        } else {
            answer.push(index - wordDict[s[index]])
            wordDict[s[index]] = index
        }
    }
    return answer;
}