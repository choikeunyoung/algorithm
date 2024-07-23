function solution(wallpaper) {
    var answer = [];
    let minX = 10 ** 9
    let maxX = 0
    let minY = 10 ** 9
    let maxY = 0
    let yCheck = 0
    for (wall of wallpaper) {
        let xCheck = 0
        for (paper of wall) {
            if (paper === "#") {
                if (minX > xCheck) {
                    minX = xCheck
                }
                if (minY > yCheck) {
                    minY = yCheck
                }
                if (maxX < xCheck) {
                    maxX = xCheck
                }
                if (maxY < yCheck) {
                    maxY = yCheck
                }
            }
            xCheck += 1
        }
        yCheck += 1
    }
    answer = [minY, minX, maxY + 1, maxX + 1]
    return answer
}