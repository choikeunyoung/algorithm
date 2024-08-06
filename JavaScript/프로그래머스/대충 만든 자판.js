function solution(keymap, targets) {
    let answer = []
    // 목표가 되는 값을 탐색
    for (target of targets) {
        // 총 몇번의 횟수를 눌러야는지 체크
        let total = 0
        // 한 문자씩 탐색
        for (tar of target) {
            // 최소 누르는 횟수 체크
            let minValue = 10 ** 9
            // 키보드 자판 반복
            for (key of keymap) {
                // 인덱스를 통해서 몇번 누르는지 체크
                const value = key.indexOf(tar)
                // 값이 있고 minValue 보다 작은 값인 경우 값 갱신
                if (value < minValue && value !== -1) {
                    minValue = value + 1
                }
            }
            // total 값 갱신
            total += minValue
        }
        // 초기 선언한 값보다 큰 경우 -1 로 갱신해줌 만들 수 없기 때문에
        if (total >= 10 ** 9) {
            total = -1
        }
        answer.push(total)
    }
    return answer;
}