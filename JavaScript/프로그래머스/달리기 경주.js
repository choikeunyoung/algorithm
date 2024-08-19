function solution(players, callings) {
  let playerIndexMap = new Map();

  players.forEach((player, index) => {
    playerIndexMap.set(player, index);
  });

  for (let calling of callings) {
    let currentIndex = playerIndexMap.get(calling);
    if (currentIndex > 0) {
      let previousPlayer = players[currentIndex - 1];

      players[currentIndex - 1] = calling;
      players[currentIndex] = previousPlayer;

      playerIndexMap.set(calling, currentIndex - 1);
      playerIndexMap.set(previousPlayer, currentIndex);
    }
  }

  return players;
}
