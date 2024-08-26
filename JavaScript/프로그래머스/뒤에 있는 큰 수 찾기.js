function solution(numbers) {
  let answer = [];
  let stack = [];
  let maxNumber = 0;
  for (let i = numbers.length - 1; i >= 0; i--) {
    if (stack.length > 0) {
      if (numbers[i] >= maxNumber) {
        maxNumber = numbers[i];
        answer.push(-1);
        stack = [];
        stack.push(maxNumber);
      } else {
        while (true) {
          if (numbers[i] < stack[0]) {
            answer.push(stack[0]);
            stack.unshift(numbers[i]);
            break;
          } else {
            stack.shift();
          }
        }
      }
    } else {
      maxNumber = numbers[i];
      stack.push(numbers[i]);
      answer.push(-1);
    }
  }
  answer.reverse();
  return answer;
}
