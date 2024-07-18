function solution(name, yearning, photo) {
    const answer = []
    for (person of photo) {
        let ans = 0
        for (per of person) {
            name.forEach((people, index) => {
                people == per ? ans += yearning[index] : null
            })
        }
        answer.push(ans)
    }
    return answer
}