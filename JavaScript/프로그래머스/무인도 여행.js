function solution(maps) {
  let answer = [];
  //   행의 개수
  const rowLength = maps[0].length;
  //   열의 개수
  const columnLength = maps.length;
  //   방향 배열
  const direction = [
    [0, -1],
    [-1, 0],
    [0, 1],
    [1, 0],
  ];
  //   DFS함수
  const DFS = (x, y) => {
    // 칸을 움직이며 더해나가는 변수
    let total = 0;
    // 방문처리
    visited[x][y] = true;
    // 스택
    stack = [[x, y]];
    // 스택 길이가 0보다 클때까지
    while (stack.length > 0) {
      // stack 첫 인자 추출
      const [nextX, nextY] = stack.shift();
      //   Number로 변환 후 더해나감
      total += Number(maps[nextX][nextY]);
      //   방향배열
      for (let k = 0; k < 4; k++) {
        const nx = nextX + direction[k][0];
        const ny = nextY + direction[k][1];
        // 범위 내 존재
        if (0 <= ny && ny < rowLength && 0 <= nx && nx < columnLength) {
          // X 가 아니고 방문처리가 되지 않았을 경우
          if (maps[nx][ny] !== "X" && visited[nx][ny] === false) {
            // 방문 처리 후 스택에 저장
            visited[nx][ny] = true;
            stack.push([nx, ny]);
          }
        }
      }
    }
    // 더해나간 값 리턴
    return total;
  };
  // 2차원 배열 생성 (ES6부터 가능)
  let visited = Array.from(Array(columnLength), () =>
    Array(rowLength).fill(false)
  );
  // 배열 탐색
  for (let mapIndex = 0; mapIndex < columnLength; mapIndex++) {
    for (let index = 0; index < rowLength; index++) {
      // X가 아니고 방문하지 않았을 때
      if (maps[mapIndex][index] !== "X" && visited[mapIndex][index] === false) {
        answer.push(DFS(mapIndex, index));
      }
    }
  }
  // answer 변수에 숫자가 존재할 경우 sort 처리 아닐 경우 -1
  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}
