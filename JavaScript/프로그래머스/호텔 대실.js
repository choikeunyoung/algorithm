function solution(book_time) {
  // 정답 값 리턴
  let answer = 0;
  // 들어온 시간 값 map을 통해서 리턴
  let sortedList = book_time.map((time) => {
    // 시작 시간 : 를 기준으로 Number로 치환 후 리턴
    let [...start] = time[0].split(":").map((value) => Number(value));
    //   끝나는 시간 : 를 기준으로 Number로 치환 후 리턴
    let [...end] = time[1].split(":").map((value) => Number(value));
    //   시작 시간과 끝나는 시간 분으로 치환
    start = start[0] * 60 + start[1];
    end = end[0] * 60 + end[1];
    //   시작, 끝 분으로 변환한 값 리턴
    return [start, end];
  });
  //   리스트 정렬
  sortedList.sort((a, b) => a[0] - b[0]);
  //   반복문을 통해서 answer 증가
  for (let i = 0; i < sortedList.length; i++) {
    answer += 1;
    // i 번인덱스까지 반복문 동작
    for (let j = 0; j < i; j++) {
      // 현재 i 번 인덱스의 시작 시간이 이전에 들어온 끝나는 시간 + 10 보다 크거나 같은 경우
      if (sortedList[i][0] >= sortedList[j][1] + 10) {
        // answer 1 감소
        answer -= 1;
        // 끝나는 시간 24:00 으로 갱신 처리 하여 방을 나왔다는 체크
        sortedList[j][1] = 1440;
        break;
      }
    }
  }
  return answer;
}
