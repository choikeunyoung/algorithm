function solution(cards1, cards2, goal) {
  var answer = "";
  let card1Length = cards1.length;
  let card2Length = cards2.length;
  let goalLength = goal.length;
  let index1 = 0;
  let index2 = 0;
  let flag = 0;
  while (goal.length > 0) {
    flag = 0;
    if (index1 < card1Length) {
      if (cards1[index1] === goal[0]) {
        index1 += 1;
        goal.shift();
        continue;
      } else {
        flag = 1;
      }
    }

    if (index2 < card2Length) {
      if (cards2[index2] === goal[0]) {
        flag = 0;
        index2 += 1;
        goal.shift();
        continue;
      } else {
        flag = 1;
      }
    }

    if (flag === 1) {
      break;
    }
  }

  if (flag === 1) {
    answer = "No";
  } else {
    answer = "Yes";
  }
  return answer;
}
