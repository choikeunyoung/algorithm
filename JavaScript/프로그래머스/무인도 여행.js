function solution(maps) {
  let answer = [];
  const rowLength = maps[0].length;
  const columnLength = maps.length;
  const direction = [
    [0, -1],
    [-1, 0],
    [0, 1],
    [1, 0],
  ];
  const DFS = (x, y) => {
    let total = 0;
    visited[x][y] = true;
    stack = [[x, y]];
    while (stack.length > 0) {
      const [nextX, nextY] = stack.shift();
      total += Number(maps[nextX][nextY]);
      for (let k = 0; k < 4; k++) {
        const nx = nextX + direction[k][0];
        const ny = nextY + direction[k][1];
        if (0 <= ny && ny < rowLength && 0 <= nx && nx < columnLength) {
          if (maps[nx][ny] !== "X" && visited[nx][ny] === false) {
            visited[nx][ny] = true;
            stack.push([nx, ny]);
          }
        }
      }
    }
    return total;
  };

  let visited = Array.from(Array(columnLength), () =>
    Array(rowLength).fill(false)
  );

  for (let mapIndex = 0; mapIndex < columnLength; mapIndex++) {
    for (let index = 0; index < rowLength; index++) {
      if (maps[mapIndex][index] !== "X" && visited[mapIndex][index] === false) {
        answer.push(DFS(mapIndex, index));
      }
    }
  }

  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}
