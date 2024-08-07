function solution(t, p) {
    let answer = 0
    let cnt = 0
    // p 길이 체크
    pLength = p.length
    // t 길이 - p 길이 까지 반복문 진행
    for (let i = 0; i <= t.length - pLength; i++) {
        // slice 를 진행하여 문자를 분해
        const checkNumber = Number(t.slice(i, i + pLength))
        // Number로 치환 후 값 비교
        if (checkNumber <= Number(p)) {
            cnt += 1
        }
    }
    answer = cnt
    return answer;
}